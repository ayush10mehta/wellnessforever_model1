#importing libraries
import pandas as pd
from flask import Flask, render_template, request

#declare the app
app = Flask(__name__)

#start the app route which is '/'
@app.route('/', methods=['GET'])
#declare the main function
def main():
    return render_template('index.html')

#form submission route
@app.route('/score',methods=['POST'])
def score():
    #extract the data from post request
    print("success")
   
    


    return render_template('score.html', score = 300 )


if __name__ == "__main__":
    app.run(debug=True)
    

