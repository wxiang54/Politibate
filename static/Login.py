#!/usr/bin/python
print "content-type: text/html\r\n"

import cgi
import cgitb
cgitb.enable()
import md5
import random
import os

m = md5.new()
ip = os.environ["REMOTE_ADDR"]
info = open('Users.txt', 'a')
loggedIn = open('loggedin.txt', 'a')
keys = cgi.FieldStorage()

htmlH = '''<!DOCTYPE HTML>      
            <html>
            <head>
                <title></title>
            </head>
            <body>
            <link rel="stylesheet" type="text/css" href="Login.css">
            <form method="POST" action="Login.py">'''
htmlE = '</form></body></html>'
AccountForm ='''
        <table>
        <tr> <td>Create an Account</td> </tr>
        <tr> <td>Username</td><td><input type="text" name="UserA" size="20" value=""></td> </tr>
        <tr> <td>Password</td><td><input type="password" name="PassA" size="20" value=""></td> </tr>
        <tr> <td>Retype Password</td><td><input type="password" name="RePass" size="20" value=""></td> </tr>
        <tr><td><input type="submit" name="Submit" value="Create!"></td> </tr>
        </table><br>'''
LogInForm = '''
            <table>
            <tr> <td>Log in to your account</td></tr>
            <tr> <td>Username</td><td><input type="text" name="User" size="20" value=""></td> </tr>
            <tr> <td>Password</td><td><input type="password" name="Pass" size="20" value=""></td> </tr>
            <tr> <td><input type="submit" name="Submit" value="Login"></td> </tr>
            </table>'''
Unmatch = 'Your passwords do not match! Go back and try again.'
ItWorked = '''Your account has been created.<br>
            <a href = "Login.py">Log in</a>'''
UserUsed = 'Sorry, the username you chose is already in use, please select another one'
Success = 'You have successfully logged in<br>'
Failure = '''Your password and your username do not match/this username does not exist/you are already logged in, please
            <a href = "Login.py">try again</a>'''
Unsecure = 'Your password does contain a number or is at least 6 characters, pick another one'
hasSpecialChar = 'Your username has invalid characters, pick another one'
NotFilled = 'Please fill in both the username and the password'

def mainpage():
    webpage = ''
    if len(keys) == 0: #default page without keys
        webpage = htmlH + '<h1>Make an Account! or Sign up!</h1>'+ AccountForm + LogInForm+htmlE
    elif 'Submit'in keys and keys['Submit'].value == 'Create!': #creates an account 
        webpage = htmlH + CreateAccount() + htmlE
    else:               #log in
        webpage = htmlH + LogIn() + htmlE
    return webpage

def CreateAccount():
    read = open('Users.txt', 'r').read()
    hasNumber = False                               #used to check if the password has a number
    isValid = True
    if 'UserA' not in keys or 'PassA' not in keys or 'RePass' not in keys: #tells the user if they are missing a field
        return NotFilled
    else:
        Username = keys['UserA'].value.lower()
        Password = keys['PassA'].value
    if Password == keys['RePass'].value:
        for i in range(9):  #checks for number in the password
            if str(i) in Password:
                hasNumber = True
        for l in Username: #makes sure only numbers and letters are allowed in the username
            if not ('A' <= str(l) <= 'Z' or 'a' <= str(l) <= 'z' or '0' <= str(l) <= '9'): 
                isValid = False
        if hasNumber == False or len(Password) < 6: #checks length of the password
            return Unsecure
        if isValid == False: #tells the user their name is invalid
            return hasSpecialChar
        elif Username not in read:     #checks if the username is already in use, if not makes an account
            m.update(Password)
            hashedPassword = m.hexdigest()
            info.write(Username + ',')
            info.write(hashedPassword + '\n')
            return ItWorked
        elif str(Username) in read:
            return UserUsed
    elif not Password == keys['RePass'].value:  #tells the user their passwords don't match
        return Unmatch
def remove(user):
    loggedIn = open('loggedin.txt', 'r').readlines()
    newfile = ''
    for line in loggedIn:
        if not user in line:
            newfile += line 
    newloggedIn = open('loggedin.txt', 'w')
    newloggedIn.write(newfile)
    newloggedIn.close()
def LogIn():
    accounts = open('Users.txt', 'r').read()  
    loggedIn = open('loggedin.txt', 'a')
    loggedInR = open('loggedin.txt', 'r').read() 
    username = keys['User'].value.lower()
    if 'User' not in keys or 'Pass' not in keys: #tells the user if they are missing a field
        return NotFilled  
    else:
        m.update(keys['Pass'].value)  
        hashedPassword = m.hexdigest()
        loginfo = username + ','+ hashedPassword
    if (loginfo in accounts) and (username not in loggedInR): #checks if the user is existing and whether they are logged in or not
        magicNumber = str(random.randint(1000000, 9999999))
        loggedIn.write(keys['User'].value + ','+ magicNumber + ',' + ip+ '\n') #adds the user to the logged in file
        link = ('<a href = "mainpage.py?user=' 
                + username + '&id=' + magicNumber+ '">Go to the main page</a>')
        return Success + link #gives the user a link to the main page
    else:
        return Failure

print mainpage()
info.close()
loggedIn.close()