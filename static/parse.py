from flask import flask
import csv
def parse():
    newtext=''	
    basetext= '''<select name="subjects" size ="1">'''
    f=open('topics.csv','r')
    subjectlist= f.read()
    splited=subjectlist.split("\n")
    f.close()
    for k in range(len(splited)):
        mylist = []
        sub=splited[k].split(",")
        for j in sub:
            mylist.append(j)
        splited[k] = mylist 
    return splited
print parse()
