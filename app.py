import joblib

def predict_specie(sl, sw, pl, pw):
    model = joblib.load('iris-deploy.pkl')
    prediction = model.predict([[sl,sw,pl,pw]])
    # 0 - Setosa

    if prediction ==0:
        return 'Setosa'

    # 1 - Versicolor
    
    elif prediction == 1:
        return 'Versicolor'

    # 2 - Virginica

    else:
        return 'Virginica'

import flask
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #extract the data from post request
    sl = float(request.form['sl'])
    sw = float(request.form['sw'])
    pl = float(request.form['pl'])
    pw = float(request.form['pw'])
    prediction= predict_specie(sl,sw,pl,pw)
    return render_template('predict.html',species=prediction)


if __name__ == '__main__':
    app.run()

  