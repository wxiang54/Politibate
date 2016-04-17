from flask import Flask, render_template
import os
from util import *

app = Flask(__name__)

@app.route('/politibate')
def homepage():
    try:
        title = "PolitiBate"
        return render_template("template.html",title=title)
    except Exception,e:
        return str(e)

@app.route('/login')
def login():
    try:
        title = "Login"
        pageType = "login"
        return render_template("template.html",title=title,pageType=pageType)
    except Exception,e:
        return str(e)

@app.route('/politibate/verify')
def verifyUser():
    try:
        usernm = "will"
        passwd = "test"
        correctCreds = verify(usernm, passwd)
        return render_template("login.html", body = str(correctCreds))
    except Exception,e:
        return str(e)


if __name__ == "__main__":
    app.run()

        
 
