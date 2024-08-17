import sys
import numpy as np
import pandas as pd
from pandas import read_csv
from sqlalchemy import create_engine

def load_data(losses_filepath): 
  try: 
    df = read_csv(losses_filepath)
    print(df.shape)
    return df
  except: 'El archivo .csv de eventos de pérdida debe estar dentro de la carpeta data'

def clean_data(df): 
  df.columns = ['date', 'losses']
  df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
  df['year'] = df['date'].dt.year
  df['periodo'] = df['date'].dt.to_period('M').astype(str)
  df['date'] = df['date'].dt.date
  df['losses'].fillna(0, inplace=True)
  return df

def save_data(df): 
  engine = create_engine(f'sqlite:///data/Losses.db')
  df.to_sql('Losses', engine, index=False, if_exists='replace')

def main(): 
  
  if len(sys.argv) == 2: 
    losses_filepath = sys.argv[1:]
    print(losses_filepath)
    
    print('Loading data...\n    LOSSES: {}'.format(losses_filepath))
    df = load_data(losses_filepath[0])
    print(df.shape)
    
    print('Cleaning data...')
    df = clean_data(df)
    
    print('Saving data...\n    DATABASE: Losses.db')
    save_data(df)
    
    print('Cleaned data saved to database!')
    
  else: 
    print(
      'Please provide the filepath of the losses dataset as the first argument'\
      '\n\nExample: python process_data.py '\
      'losses.csv '\
    )
    
if __name__ == '__main__':
  main()