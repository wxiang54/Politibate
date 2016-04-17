import sys
import hashlib as hsh

# Verify a user using users.csv
def verify(usernm, passwd):
    f=open('/var/www/FlaskApp/FlaskApp/users.csv','r')
    userList= f.read().split("\n")
    f.close()
    for user in userList:
        user = user.split(",")
        if user[0] == usernm:
            if hsh.md5(user[1]).hexdigest() == passwd:
                return True
            return False
    return False

def addUser:
    return ""
