#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")
def home():
    name='Avni Sharma'
    age='13'
    return render_template('index.html',name=name,age=age)

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
app.run()
