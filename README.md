# capstone_project
# Scenario quantification

## Project definition
With a base data of historical losses to calculate some metrics as the expected and catastrophical monthly losses.

## Analysis
To calculate the metrics we find the frequency and severity distributions that best fit the data with help of `distfit` library. In particular, the fitting of severity is did it taking as metric of evaluation the Kolmogorov Smirnov test with a 95% significance level. We have to calculate the convolution between frequency and severity distributions, for this convolution we do Monte Carlo simulations.

## Conclusions
This project was effective calculating the metrics related with the monthly aggregated losses, you can use it with any losses data with two minimum fields, date and loss amount. **Please name your minimum fields as date and losses.**

## Installations
You can run this poject downloading the app, data and model folders in a root directory in your local machine so your folder have the next structure:

root directory/
├──app/
|  ├──templates/
|     ├──master.html
|  run.py
├──data/
|  ├──losses.csv
|  ├──process_data.py
├──model/
|  ├──model.py

The app folder directory the html and python files to deploy de web app. The data directory has the data and the python file to preproccess it, and in the model folder the python file with the code to do the Monte Carlo simulations.

This project was developed with Python 3.10.8 and the next versions of the next libraries:
* `distfit 1.8.0` (see installation command below)
* `Flask 3.0.3` (see installation command below)
* `joblib 1.4.2`
* `numpy 2.0.1`
* `pandas 2.2.2`
* `plotly 5.23.0` (see installation command below)
* `pypickle 1.1.0`
* `scikit-learn 1.5.1` (see installation command below)
* `scipy 1.14.0`
* `SQLAlchemy 2.0.32` (see installation command below)

To install the libraries please run these commands in your root directory:
``pip install -U distfit``
``pip install flask``
``pip install plotly==5.23.0``
``pip install scikit-learn``
``pip install sqlalchemy``

## Deploy instructions
1. Run the following commands in the root directory to set up the database and simulations.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/losses.csv`
    - To run statistical pipeline that fit frequency and severity probability distributions to data and save the monte carlo simulations
        `python model/model.py`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

## Motivation
The project is useful to automatize the process the Monte Carlo simulations of the aggregated losses for an scenario analysis of any financial risk, as an example, it uses base information as the historical data of losses to give the expected and the catastrofical losses (quantile 0.999). You will see the results in the web app, some important plots of data and simulations will plotted.

## Results
With the development of this project we can provide a time series of losses which we want to get the monthly expected and catastrophical losses. For this we fit the severity distribution using `distfit` and getting the distribution fitted name, the associated parameters and the p-value; and for frequency we use a Poisson distribution with the monthly frequency mean as parameter. With this distributions a Monte Carlo simulation is performed so we get the monthly measures of losses and its plots in the web app are deployed.

## Acknowledgements
Special acknoledgements to all Python community who give their knoledgement to contribute to develop tools as this one what I offer to you all. So, please feel you free to use it!
