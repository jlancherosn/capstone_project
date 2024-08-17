from distfit import distfit
import inspect
import numpy as np
import pandas as pd
from pandas import read_csv, read_excel, read_sql_table
import pickle
from scipy import stats
from sqlalchemy import create_engine

def load_data():
  '''
  Load data from database named Losses.db
  INPUT: 
    None
  OUTPUT: 
    df: (Pandas DataFrame) DataFrame with the data of losses
  '''
  engine = create_engine(f'sqlite:///data/Losses.db')
  df = read_sql_table('Losses', engine)
  return df

def frequency_model(df): 
  '''
  Calculate the Poisson parameter mu
  INPUT: 
    df: (Pandas DataFrame) DataFrame with the data of losses
  OUTPUT: 
    mu: (float) Poisson parameter mu
  '''
  frequencies = df['periodo'].value_counts().sort_index()
  mu = frequencies.mean()
  print('The Poisson parameter is:', mu)
  return mu

def severity_model(df):
  '''
  Fit the severity distribution
  INPUT: 
    df: (Pandas DataFrame) DataFrame with the data of losses
  OUTPUT: 
    severity_distribution: (str) Name of the severity distribution
    parameters_str: (str) Parameters of the severity distribution
    loc: (float) Location parameter of the severity distribution
    scale: (float) Scale parameter of the severity distribution
  '''

  severity_model = distfit(alpha=0.05, bins=50, stats='ks')
  severity_model.fit_transform(df['losses'], verbose=1)
  model = severity_model.model

  severity_distribution = model['name']
  print('The fitted severity distribution is:', severity_distribution)
  sig = eval(f'inspect.signature(stats.{severity_distribution}._pdf)')
  arg_names = [p for p in sig.parameters.keys() if p not in ['self', 'x']]
  arg_values = [x for x in model['arg']]
  parameters_str = ', '.join([f'{v}' for v in arg_values])
  loc, scale = model['loc'], model['scale']

  parameters_dict = {}
  [parameters_dict.update({arg_names[0]: x}) for i, x in enumerate(model['arg'])]
  parameters_dict.update({'loc': loc})
  parameters_dict.update({'scale': scale})
  print('The severity distribution parameters are:', parameters_dict)

  # goodness of fit
  res = stats.goodness_of_fit(
    dist=eval(f"stats.{model['name']}"),
    data=df['losses'], statistic='ks', 
    fit_params=parameters_dict,
    n_mc_samples=1000,
    random_state=17
  )
  print('The pvalue of goodness of fit is', res.pvalue, '!')

  return severity_distribution, parameters_str, loc, scale

def monte_carlo(mu, severity_distribution, parameters_str, loc, scale): 
  '''
  Simulate the losses using the Monte Carlo method
  INPUT: 
    mu: (float) Poisson parameter mu
    severity_distribution: (str) Name of the severity distribution
    parameters_str: (str) Parameters of the severity distribution
    loc: (float) Location parameter of the severity distribution
    scale: (float) Scale parameter of the severity distribution
  OUTPUT: 
    simulations: (list) List of simulated losses
  '''

  simulations = []

  for i in range(100000): 
    frequency = int(stats.poisson.ppf(q=stats.uniform.rvs(size=1), mu=mu))
    simulations.append(np.sum(eval('stats.{}.rvs({}, loc={}, scale={}, size={})'.format(severity_distribution, parameters_str, loc, scale, frequency))))

  print(pd.Series(simulations).describe(percentiles=[x/100 for x in range(10, 91, 10)] + [0.95, 0.999]).to_string())
  
  return simulations

def save_simulations(simulations):
  with open('model/monte_carlo_simulations.pkl', 'wb') as fp:
    pickle.dump(simulations, fp)

def main():

  print('Loading data...\n    DATABASE: Losses.db')
  df = load_data()
  
  print('Building frequency model...')
  mu = frequency_model(df)

  print('Building severity model...')
  severity_distribution, parameters_str, loc, scale = severity_model(df)
  
  print('Monte Carlo simulations...')
  simulations = monte_carlo(mu, severity_distribution, parameters_str, loc, scale)

  print('Saving simulations...')
  save_simulations(simulations)

  print('Monte Carlo simulations saved!')

if __name__ == '__main__':
    main()