from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
import pandas as pd

application = Flask(__name__)
app =application

# Load the trained model
with open('XGBClassifier_final.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the MinMaxScaler
with open('MinMaxScaler.pkl', 'rb') as file:
    scaler, df1 = pickle.load(file)


label_encoder = LabelEncoder()

@app.route('/')
def home():
    return render_template('churn.html')



@app.route('/predict', methods=['POST'])
def predict():
   
  



 # Extract input data from the request
    senior_citizen = int(request.form['senior_citizen'])
    partner = int(request.form['partner'])
    dependents = int(request.form['dependents'])
    tenure = float(request.form['tenure'])
    online_security = int(request.form['online_security'])
    online_backup = int(request.form['online_backup'])
    device_protection = int(request.form['device_protection'])
    tech_support = int(request.form['tech_support'])
    contract = int(request.form['contract'])
    paperless_billing = int(request.form['paperless_billing'])
    payment_method = int(request.form['payment_method'])
    monthly_charges = float(request.form['monthly_charges'])
    total_charges = float(request.form['total_charges'])
    

    # Preprocess the input data
    df = pd.DataFrame({
        
        'SeniorCitizen': [senior_citizen],
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'OnlineSecurity': [online_security],
        'OnlineBackup': [online_backup],
        'DeviceProtection': [device_protection],
        'TechSupport': [tech_support],
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })

    # # Encode categorical features
    # for column in df.select_dtypes(include='object'):
    #     df1[column] = label_encoder.fit_transform(df1[column])
    # Apply the same preprocessing transformations as in the ML.ipynb notebook


    df['tenure'] = scaler.fit_transform(df[['tenure']])
    df['MonthlyCharges'] = scaler.fit_transform(df[['MonthlyCharges']])
    df['TotalCharges'] = scaler.fit_transform(df[['TotalCharges']])
    
    # Make predictions using the loaded model
    prediction = model.predict(df)

    if prediction == 1:
        result = "Churn"
    else:
        result = "No Churn"
    # result= 'Churn'

    return render_template('churn.html', prediction=result)
    
    # # Return the prediction to the user interface
    # return render_template('churn.html', prediction=prediction)
    
    # output = prediction[0]
    # return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)

