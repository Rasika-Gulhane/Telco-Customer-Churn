# Telco-Customer-Churn


## Introduction:


In today's highly competitive business landscape, customer retention plays a crucial role in the success and sustainability of any organization. Understanding and predicting customer behavior are key factors in developing effective customer retention strategies. Machine learning models offer a powerful tool for analyzing vast amounts of customer data and deriving valuable insights to drive decision-making.

### ML-Model-Flask-Deployment
Machine Learn Models are deployed on production using Flask API


### Dataset: 
![TelcoCustomerChurn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Project Structure
This project has four major parts :
1. EDA_&_Modules.ipynm - This contains code for our Machine Learning models to predict Customer Retentions
2. FinalizedModule - Choosed BestModule after Tuning and Pickled it for further production.
3. app.py - This contains Flask APIs that receives Customer details through GUI or API calls, computes the precited value based on our model and returns it.
4. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
5. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.


### Running the project

##How to Run the project:

Install all the libraries mentioned in the requirements.txt file.
Clone this repository in your local system.
Open the command prompt from your project directory and run the command python app.py.
Go to your browser and type http://127.0.0.1:8080 in the address bar.
Hurray! That's it.

1. Ensure that you are in the project home directory. Create the machine learning model by running below command -

```
XGBClassifier_final.pkl
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 8080.

3. Navigate to URL http://localhost:8080

You should be able to view the homepage as shown in report below :
(https://docs.google.com/document/d/1z5hfzp3Y-IAYC1nVokkBiPrSBikiXI4Dt-IjChoPQsU/edit#)

Enter valid values in all input boxes and hit Predict.

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
-
