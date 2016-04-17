import sys
import hashlib as hsh
import os.path

# Verify a user using users.csv
def verify(username, password):
    #0: Success
    #1: Username exists, but password wrong
    #2: Username doesn't exist
    f=open('/var/www/FlaskApp/FlaskApp/users.csv','r')
    userList= f.read().split("\n")
    f.close()
    for user in userList:
        user = user.split(",")
        if username == user[0]:
            if hsh.md5(password).hexdigest() == user[1]:
                return 0
            return 1
    return 2


def addUser(username, password, rpassword):
    #0: Success
    #1: Username field left blank
    #2: One of the password fields left blank
    #3: pass and rpass don't match
    #4: user already exists in users.csv
    
    if username.strip() == "":
        return 1

    if password.strip() == "" or rpassword.strip() == "":
        return 2
        
    if password != rpassword:
        return 3
    
    f=open('/var/www/FlaskApp/FlaskApp/users.csv','r+')
    userList= f.read().split("\n")

    for user in userList:
        user = user.split(",")
        if user[0] == username:
            return 4

    fillTopics(f, username, password)
    f.close()
    return 0


def fillTopics(f, username, password):
    retStr = "%s,%s," % (username, hsh.md5(password).hexdigest())
    
    topics = open('/var/www/FlaskApp/FlaskApp/topicRef.txt','r').read().split("\n")
    for topic in topics:
        retStr += "%s=%s," % (topic,"none")

    retStr = retStr[:-1] + "\n"
           
    f.write( retStr )
    


def updateRoom(room, username, comment):
    roomHTML = open("/var/www/FlaskApp/FlaskApp/templates/debateRooms/%s.html" % room, "r")
    roomRead = roomHTML.read().split("<!-- TAGLINE -->")
    
    commentToAdd = '''
  <tr><td style="width:40px"><b> %s:</b> &nbsp; %s </td></tr>
<!-- TAGLINE -->
  ''' % (username, comment)
    
    roomHTML.close()

    roomHTML = open("/var/www/FlaskApp/FlaskApp/templates/debateRooms/%s.html" % room, "w")
    roomHTML.write(roomRead[0] + commentToAdd + roomRead[1])
    roomHTML.close()


def chPos(username, password, topic, position):
    f=open('/var/www/FlaskApp/FlaskApp/users.csv','r')
    userList= f.read().split("\n")
    
    for user in userList:
        userData = user.split(",")
        usernameFromData = userData[0]
        if username == usernameFromData:
            topicPos = user.find(topic)
            userT = user[topicPos:]
            topicData = userT[:userT.find(",")]
            oldTopic = topicData.split("=")[1]

            newTopicData = "%s=%s" % (topic,position)
            globVar = user.replace(topicData,newTopicData)
            
    #rebuild string
    retStr = "";
    for user in userList:
        if username != user.split(",")[0]:
            retStr += user + "\n"
        else:
            retStr += globVar + "\n"
    f.close()
    f = open('/var/www/FlaskApp/FlaskApp/users.csv', 'w')
    f.write(retStr)
    f.close()






