# Two-Wheeler-Loan-Default-Prediction

![Alt txt](https://www.billsbills.com/sites/www.billsbills.com/files/16827350035_de793ca7ad_k.jpg)



## Problem Statement <br/>

Financial institutions incur significant losses due to the default of vehicle loans. This has led to the tightening up of two wheeler loan underwriting and increased vehicle loan rejection rates. The need for a better credit risk scoring model is also raised by these institutions. This warrants a study to estimate the determinants of loan default. My Job is to accurately predict the probability of loanee/borrower defaulting on a vehicle loan in the first EMI (Equated Monthly Instalments) on the due date. Following Information regarding the loan and loanee are provided in the dataset.

Loanee Information (Demographic data like age, income, Identity proof etc.) Loan Information (Disbursal details, amount, EMI, loan to value ratio etc.) Bureau data & history (Bureau score, number of active accounts, the status of other loans, credit history etc.) Doing so will ensure that clients capable of repayment are not rejected and important determinants can be identified which can be further used for minimising the default rates.

## Evaluation Metric

* ROC-AUC Score

## Approach Taken To Solve The problem

1. Collecting Data from publicly availaible website <br/>
2. Data Preprocessing <br/>
3. Data Analysis & Visualisation <br/>
4. Feature Selection <br/>
5. Creating Machine Learning Model to predict if a person if a is potential loan due defaulter or not <br/>
6. Model Explainability (Using Libraries like SHAP to find out most important features and also learn how different features are contributing for final prediction) <br/>
7. Created a pickle file of model for using it with web application

## Creating Customer Interface for the project

1. Created a website using HTML & CSS 
2. Integrated the ML model with frontend using flask
3. Deployed the web application in Heroku app server 

## Test Values to try for website

* Customer Related information
1.Disbursed Amount - 41094
2.Asset cost - 65687
3.LTV -63.48

* Vehicle Related information

1.Branch id - 34 
2. Employment Type -2
3. State Id -992

* Customer Related Information
1 Total Current Balance-0
2. Total Accounts - 1
3. Delinquent Accts in last 6 mnths - 0
4. perform cns score -825
5. Age-34


### Link To Website : https://loandefault2-api.herokuapp.com/

## Things to learn from the project :

1. Data preprocessing.
2. Data analysis.
3. Machine Learning Modelling.
4. Model Explainability.
5. HTML, Css & flask.

### Linkedin : https://www.linkedin.com/posts/pancham-desai-7a9357188_finally-after-working-hard-for-past-1-month-activity-6712290023468875776-buyN
