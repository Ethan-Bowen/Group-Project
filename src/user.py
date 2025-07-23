import os
from passwordBank import HashMap

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.passwordBank = HashMap(10)
        # self.passwordFile = open("passwords.txt")

    def createUser(self, username, password):
        user = User(username, password)
        if os.path.isdir(username):
            return "This user already exists!"
        else:
            os.mkdir(username)
            