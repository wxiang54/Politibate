from flask import Flask, request, render_template, redirect, url_for, make_response
from util import *
import hashlib as hsh
import time

app = Flask(__name__)


@app.route('/politibate/')
def homepage():
    try:
        title = "PolitiBate"
        username = request.cookies.get('username')
        password = request.cookies.get('password')
        if username is not None:
            verifInt = verify(username, password)
            if verifInt != 0:
                msg = "LoginError: Cookies may have been tampered with. Try logging in again."
            else:
                welcome = "Welcome back to PolitiBate, %s!" % username
                time.sleep(1)
                return render_template("template.html", title=title, welcome=welcome, loggedIn = True)
            
        return render_template("template.html", title=title, loggedIn=False)
                    
    except Exception,e:
        return str(e)

@app.route('/politibate/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            return render_template("login.html")
        else:
            mode = request.form['mode']
            
            if mode == 'signup':
                #CHECK SIGNUP
                username = request.form['username']
                password = request.form['password']
                rpassword = request.form['rpassword']

                #0: Success
                #1: Username field left blank
                #2: One of the password fields left blank
                #3: pass and rpass don't match
                #4: user already exists in users.c
                retInt = addUser( username, password, rpassword )
                
                if retInt == 1:
                    msg = "Username cannot be left blank!"    
                elif retInt == 2:
                    msg = "Password cannot be left blank!"
                elif retInt == 3:
                    msg = "Entered Passwords do not match! Make sure to choose a password you can remember."
                elif retInt == 4:
                    msg = "Username already exists! Please choose another username."
                else: #Login successful
                    msg = "Signup successful! You can now log in with your credentials."

                if retInt == 0: #success
                    return render_template("login.html", msg = msg, color = 'green')
                else: #fail
                    return render_template("login.html", msg = msg, color = 'red')
            else: #mode = 'login'
                #CHECK LOGIN
                username = request.form['username']
                password = request.form['password']

                verifInt = verify(username, password)
                if verifInt == 1:
                    msg = "Wrong password for %s. Please log in again." % username
                elif verifInt == 2:
                    msg = "No account under username '%s'. Sign up if you haven't already!" % username
                else:
                    resp = make_response(redirect(url_for('homepage')))
                    resp.set_cookie('username', username)
                    resp.set_cookie('password', password)
                    return resp

                if verifInt != 0:
                    return render_template("login.html", msg = msg, color = 'red')


    except Exception,e:
        return str(e)


@app.route('/politibate/logout')
def logout():
    try:
        resp = make_response(redirect(url_for('homepage')))
        resp.set_cookie('username', '', expires=0)
        resp.set_cookie('password', '', expires=0)
        resp.set_cookie('room', '', expires=0)
        return resp
                    
    except Exception,e:
        return str(e)


@app.route('/politibate/topics',methods=['GET', 'POST'])
def topics():
    try:
        if request.method == 'GET':
            username = request.cookies.get('username')
            password = request.cookies.get('password')
            if username is not None:
                verifInt = verify(username, password)
                if verifInt != 0:
                    msg = "LoginError: Cookies may have been tampered with. Try logging in again."
                else:
                    return render_template("topics.html",loggedIn=True)
        else:
            position = request.form.get('position')
            topic = request.form.get('topic')
            username = request.cookies.get('username')
            password = request.cookies.get('password')
            if username is not None:
                verifInt = verify(username, password)
                if verifInt != 0:
                    msg = "LoginError: Cookies may have been tampered with. Try logging in again."
                else:
                    chPos(username, password, topic, position)
                    #msg = "Topic %s changed to %s!" % (topic, position)
                    resp = make_response(redirect( url_for('debate')))
                    resp.set_cookie('room', topic)
                    return resp
                    
    except Exception,e:
        return str(e)

@app.route('/politibate/debate', methods=['GET','POST'])
def debate():
    try:
        if request.method == 'GET':
            room = request.cookies.get('room')
            if room is not None:
                return render_template("/debateRooms/%s.html" % room)
            else:
                return "Error: Choose a topic!"
        else:
            comment = request.form.get('comment')
            room = request.form.get('room')
            username = request.cookies.get('username')
            
            updateRoom(room, username, comment)
            return render_template("/debateRooms/%s.html" % room)

            
            
    except Exception, e:
        return str(e)

    

if __name__ == "__main__":
    app.run()

        
 
