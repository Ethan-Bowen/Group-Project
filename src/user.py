import os
from passwordBank import HashMap

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.passwordBank = HashMap()
        self.file = None

    def createUser(self):
        user = User(self.username, self.password)
        if os.path.isdir(self.username):
            return "This user already exists!"
        else:
            os.mkdir(self.username)
            os.chdir(self.username)
            self.file = open("passwords.txt", "x")
            self.file.close()