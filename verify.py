import sys
import hashlib as hsh

# Verify a user from users.csv
def verify(usernm, passwd):
    f=open('users.csv','r')
    userList= f.read().split("\n")
    f.close()
    for user in userList:
        user = user.split(",")
        if user[0] == usernm:
            if user[1] == passwd:
                return True
            return False
    return False
