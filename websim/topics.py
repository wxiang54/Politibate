#!/usr/bin/python
#POLITIBATE

print "content-type: text/html\r\n"
htmlH = '''<!DOCTYPE HTML>      
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
            <title>PoitiBate!</title>

            <!-- CSS  -->
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <link href="../static/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
            <link href="../static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
            </head>
            <body>'''
def makedropdown():
    newtext=''	
    basetext= '''<select name="subjects" size ="1">'''
    f=open('subjects.txt','r')
    subjectlist= f.read()
    splited=subjectlist.split(",")
    f.close()
    for k in splited:
        newtext+='<option>'+ str(k) +'</option>'
    return basetext+newtext