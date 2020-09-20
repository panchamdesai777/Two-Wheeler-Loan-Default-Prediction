from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__,template_folder='test')

model=pickle.load(open('XGB.pkl','rb')) #Model gets loaded


cols=[]

@app.route('/')
def hello_world():
    A=0
    return render_template("Loan_Application-4.html",A=0)


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    print(int_features)
    final=np.array(int_features)
    df=pd.DataFrame(final.reshape(1,-1),columns=model.get_booster().feature_names)
    prediction=model.predict_proba(df) #prediction based on input features
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    print(output) #final output

    if output > str(0.50):
        return render_template('Loan_Application-4.html',prediction_text='Sorry Loan Not Approved',A=1)
    else:
        return render_template('Loan_Application-4.html',prediction_text='Congrats!! Loan Approved',A=1)


if __name__ == '__main__':
    app.run(debug=True)




