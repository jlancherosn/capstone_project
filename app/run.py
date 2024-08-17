from flask import Flask
from flask import render_template, request, jsonify
import json
import numpy as np
import pandas as pd
from pandas import read_csv
import plotly
from plotly import express as px
import plotly.figure_factory as ff
from plotly import graph_objs as go
# from plotly.graph_objs import Bar
import joblib
from sqlalchemy import create_engine

app = Flask(__name__)

# load data
engine = create_engine('sqlite:///../data/Losses.db')
df = pd.read_sql_table('Losses', engine)

# load simulations
simulations = joblib.load("../model/monte_carlo_simulations.pkl")

# index webpage displays cool visuals
@app.route('/')
@app.route('/index')
def index():
  # extract data needed for visuals
  frequency = df['periodo'].value_counts().sort_index()
  periods = list(frequency.index)

  # create visuals
  graphs = [
    {
      'data': [go.Bar(x=periods, y=frequency)],
      'layout': {'title': 'Frequency', 'yaxis': {'title': 'Count'}, 'xaxis': {'title': 'Period'}}
    },
    px.histogram(df, x='losses', marginal='box', hover_data=df.columns), 
    ff.create_distplot([df['losses']], ['losses']), 
    ff.create_distplot([simulations], ['simulations']), 
  ]

  bar_chart = graphs[0]
  bar_chart['layout'].update(shapes=[
      go.layout.Shape(type='line', x0=0, x1=1, y0=np.mean(frequency), y1=np.mean(frequency), xref='paper', line=dict(color='Black', width=2, dash='dash'), label=dict(text='Promedio'))
  ])
  simulations_chart = graphs[3]
  simulations_chart['layout'].update(shapes=[
      go.layout.Shape(type='line', x0=np.quantile(simulations, q=0.95), x1=np.quantile(simulations, q=0.95), y0=0, y1=0.0001, line=dict(color='Black', width=2, dash='dash'), label=dict(text='95%'))
  ])

  # encode plotly graphs in JSON
  ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
  graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

  # render web page with plotly graphs
  return render_template('master.html', ids=ids, graphJSON=graphJSON)

def main():
  app.run(host='0.0.0.0', port=3000, debug=True)

if __name__ == '__main__':
  main()