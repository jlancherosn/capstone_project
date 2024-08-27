# Capstone_project
# Scenario quantification

## Introduction
The purpose of this project is to develop a statistical model to predict economic losses associated with financial risks, specifically credit, market, or operational risks. Financial institutions constantly face these risks, and their ability to measure and manage potential losses is crucial for ensuring financial stability.

**Problem Statement**
The main problem addressed in this project is the accurate prediction of economic losses due to financial risk events. Identifying the factors that influence these losses and developing a predictive model will enable institutions to make informed decisions to mitigate these risks.

**Significance**
Managing financial risks is essential for institutions operating in highly volatile markets. By developing an efficient predictive model, potential losses can be estimated, allowing for proactive mitigation strategies. This not only improves financial stability but also optimizes capital allocation, ensuring institutions comply with regulatory requirements and maintain solvency.

## Dataset Overview
The dataset used in this project is a CSV file containing two key columns: date and loss. These columns provide the minimum necessary information to operate the economic model for predicting financial losses.

Source: The dataset is provided alongside the project code as an anonymized sample dataset. It functions as an illustrative example for building the economic model.
Format: CSV file with two columns:
date: The date of the recorded financial event.
loss: The amount of financial loss associated with the event on the given date.

**Variable Significance**
* date: This variable represents the time dimension of the financial loss data. It is essential for identifying trends or patterns in the occurrence of financial loss events over time, which could be important for making temporal predictions.

* loss: The loss variable quantifies the economic impact of each financial event. It is the primary dependent variable that the model aims to predict. Accurately modeling this variable allows financial institutions to anticipate potential losses and implement mitigation strategies accordingly.

**Importance to the Problem**
Given that financial institutions need to predict and manage risk, the combination of date and loss data provides a foundation for constructing a time-series model or other relevant statistical models. By analyzing historical loss data, the model can forecast future losses and help institutions prepare for potential financial downturns.

## Approach and Methodology
To address the problem of predicting economic losses due to financial risks, we employ an Aggregate Loss Distribution Approach. This approach involves combining the frequency and severity distributions of financial losses to model the total loss distribution effectively. The methodology includes the following steps:

**1. Frequency Distribution:**

This represents the number of financial loss events occurring over a specific period. It can be modeled using various statistical distributions, such as Poisson or Negative Binomial distributions, depending on the nature of the data.

**2. Severity Distribution:**

This represents the magnitude of losses associated with each event. Common distributions used for modeling severity include the Exponential, Gamma, or Pareto distributions, depending on the characteristics of the loss data.

**3. Convolution of Distributions:**

The total loss distribution is obtained by convolving the frequency and severity distributions. Mathematically, if $F(x)$ represents the cumulative distribution function (CDF) of the frequency distribution and $S(x)$ represents the CDF of the severity distribution, the convolution can be expressed as:

$$L(x) = \int_{0}^{x} f(x - y) \dot s(y) dy$$

where $f(x)$ is the probability density function (PDF) of the frequency distribution and s(x) is the PDF of the severity distribution. This integral calculates the total loss distribution by combining the frequency and severity data.

**4. Monte Carlo Simulations:**

Monte Carlo simulations are used to estimate the aggregate loss distribution by generating random samples based on the frequency and severity distributions. The process involves the following steps:

1. Simulate Number of Events: For each simulation run, draw a random number from the frequency distribution to determine the number of loss events.
2. Simulate Loss Amounts: For each event, draw random loss amounts from the severity distribution.
3. Aggregate Loss Calculation: Sum the loss amounts for each simulation run to compute the total loss.
   
Mathematically, if $N$ represents the number of simulations, $E_{i}$ is the number of events in the $i-th$ simulation, and $\lbrace L_{i, j} \rbrace_{j=1}^{E_i}$ are the simulated loss amounts for the $i-th$ simulation, the total loss for the $i-th$ simulation can be expressed as:

$$T_i = \sum_{j=1}^{E_i} L_{i, j}.$$

The aggregate loss distribution is then approximated by the empirical distribution of $\lbrace T_i \rbrace_{i=1}^{N}$, which represents the total losses over all simulations.

$$\hat{L}(x) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}(T_{i} \leq x)$$

where $\mathbb{I}(T_{i} \leq x)$ is an indicator function that equals $1$ if $T_i$ is less than or equal to $x$ and $0$ otherwise. This approximation helps in estimating the probability of various levels of aggregate losses.

**Rationale Behind the Approach**
The Aggregate Loss Distribution Approach effectively models complex loss scenarios by integrating different aspects of loss events. Convolution provides a way to combine frequency and severity data into a single distribution, and Monte Carlo simulations offer a practical method to approximate this distribution, especially when analytical solutions are complex or infeasible.

## Proposed Solution Overview
The proposed solution involves developing a comprehensive model to predict economic losses due to financial risks using the Aggregate Loss Distribution Approach. The overall architecture of the solution includes several key components that work together to address the problem and achieve accurate predictions.

**Overall Architecture and Workflow**

**Data Preparation**
* Data Import and Cleaning: Load the dataset from the CSV file, which includes the date and loss columns. Perform data cleaning to handle any missing or outlier values to ensure the quality of the data used in the model.
* Feature Engineering: Although the dataset provided is minimal, additional features could be engineered if more data is available, such as economic indicators or event-specific details, to enhance model accuracy.

**Model Building**
* Frequency Distribution Modeling: Fit a statistical distribution to the frequency data (number of events per period). Common choices include Poisson or Negative Binomial distributions, depending on the data characteristics.
* Severity Distribution Modeling: Fit a statistical distribution to the severity data (magnitude of losses). Possible distributions include Exponential, Gamma, or Pareto, chosen based on the nature of the loss data.
* Convolution: Convolve the frequency and severity distributions to derive the aggregate loss distribution. This step combines the two distributions to model the total loss distribution effectively.

**Monte Carlo Simulation**
* Simulation Setup: Define the number of Monte Carlo simulations to be performed. For each simulation:
Simulate Number of Events: Generate a random number of events based on the frequency distribution.
Simulate Loss Amounts: Generate loss amounts for each event based on the severity distribution.
Calculate Total Loss: Aggregate the loss amounts for each simulation run.
* Aggregate Loss Distribution: Approximate the total loss distribution using the empirical distribution of the simulated total losses.

**Model Evaluation**
* Performance Metrics: Evaluate the model's performance using appropriate metrics, such as goodness-of-fit tests or comparing predicted losses to actual historical data (if available).
* Validation: Validate the model using techniques such as cross-validation or out-of-sample testing to ensure robustness and accuracy.

**Results Interpretation and Application**
* Analysis of Results: Interpret the aggregate loss distribution to understand the potential financial impact under various scenarios.
* Decision Support: Provide actionable insights and recommendations based on the predicted losses, helping financial institutions prepare for and mitigate risks.

**Component Integration**
* Data Preparation feeds into Model Building by providing clean and relevant data for distribution fitting.
* Model Building and Monte Carlo Simulation are interconnected, as the distributions derived from model building are used in the simulations to generate loss scenarios.
* Monte Carlo Simulation outputs feed into Model Evaluation to assess the model's predictive capability and accuracy.
* Results Interpretation and Application leverage the evaluated model to offer practical insights and recommendations for risk management.
  
**Achieving the Desired Outcome**

The integrated workflow allows for the accurate prediction of economic losses by combining theoretical models with practical simulations. By fitting frequency and severity distributions and using Monte Carlo simulations, the solution provides a robust method to estimate potential losses, ultimately supporting informed decision-making and risk management in financial institutions.

## Conclusion

**Importance of Historical Data for Frequency Modeling:**

A critical finding is the necessity of having information from multiple periods to accurately model the frequency of loss events. In the absence of such data, the simulation defaults to a Poisson distribution with a parameter representing the average number of loss events per period (monthly, in this case). This highlights the importance of longitudinal data for precise frequency modeling.
Utility of the distfit Library:

Another significant insight is the effectiveness of the distfit library for fitting the frequency distribution. This tool simplifies the process of adjusting and selecting the best-fit distribution for frequency data, improving the accuracy and efficiency of the modeling process.
Flexibility of the Model:

The model developed is adaptable and can be applied to various loss datasets with different underlying distributions. This flexibility allows the approach to be used across different contexts and financial scenarios, enhancing its practical utility.

**Success of the Proposed Solution**

The proposed solution successfully integrates statistical modeling with Monte Carlo simulations to predict economic losses from financial risks. By combining frequency and severity distributions and leveraging advanced tools for distribution fitting, the model provides a robust framework for estimating potential losses. The ability to simulate various scenarios and assess their impact ensures that the model is both accurate and practical.

**Implications and Potential Applications**

* Risk Management: The insights gained from the model can significantly aid financial institutions in managing and mitigating risks. By understanding potential loss distributions, institutions can better prepare for adverse financial scenarios and allocate resources more effectively.

* Regulatory Compliance: The model supports compliance with regulatory requirements by providing a method for estimating economic losses and ensuring adequate capital reserves to cover potential risks.

* Adaptability: The model's flexibility to accommodate different datasets and underlying distributions makes it a valuable tool for diverse financial contexts. This adaptability enables its application to various types of financial risks and loss scenarios.

In summary, the project demonstrates a successful approach to modeling economic losses, providing valuable insights for risk management and financial planning. The findings underscore the importance of comprehensive data and advanced tools in creating effective predictive models.

## Improvements

**Limitations and Challenges**
While the current model provides a robust framework for predicting economic losses, there are some limitations and challenges that could be addressed in future iterations:

* Fixed Periodicity:

The model currently operates with a fixed periodicity, specifically on a monthly basis. This limitation may not capture the nuances of data that vary over different time frames, such as weekly or quarterly losses.
Lack of Category-Specific Analysis:

The model does not yet account for different categories of losses, such as losses segmented by type of risk (e.g., credit, market, operational). This limits the ability to perform more granular analysis and predictions for specific types of financial events.

* Limited Visualizations:

While the application provides basic visualizations, there is room for improvement by adding more sophisticated and informative visualizations. These could help in better interpreting the results and communicating insights to stakeholders.

**Potential Enhancements and Future Directions**

* Flexible Periodicity:

In future versions, the project could be enhanced by allowing for flexibility in the periodicity of analysis. By incorporating different time frames (weekly, quarterly, annually), the model would be better suited to various financial scenarios and could provide more accurate predictions depending on the context.

* Category-Specific Calculations:

Another improvement would be to introduce category-specific calculations. By segmenting the data into relevant categories (e.g., type of loss, geographical region, market sector), the model could deliver more targeted insights. This would allow institutions to better understand and manage risks in different areas of their operations.

* Enhanced Visualizations:

Developing additional visualizations would greatly benefit the application. For instance, incorporating interactive dashboards, time-series plots, and distribution comparisons could provide users with a deeper understanding of the model's outputs. Enhanced visualizations would also make the model more user-friendly and easier to interpret for non-technical stakeholders.

**Conclusion**

By addressing these limitations and implementing the suggested enhancements, the project can be further improved to offer a more flexible, detailed, and user-friendly tool for predicting and managing financial losses. These improvements would not only increase the model's accuracy but also its applicability across a wider range of financial scenarios, making it an even more valuable resource for risk management and decision-making.

## Acknowledgment

We would like to express our sincere gratitude to the Python developer community, whose contributions to statistical libraries have been invaluable to the success of this project. Special thanks go to the creators and maintainers of the distfit library, which demonstrated excellent performance and was crucial in the development of the model. Their work has significantly enhanced our ability to fit statistical distributions and model economic losses with greater accuracy.

# Installations

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

# Deploy instructions
1. Run the following commands in the root directory to set up the database and simulations.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/losses.csv`
    - To run statistical pipeline that fit frequency and severity probability distributions to data and save the monte carlo simulations
        `python model/model.py`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`
