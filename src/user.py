import os
from passwordBank import HashMap
import cryption

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.passwordBank = HashMap()
        key = None

    #Used to create a folder and txt file for a new user
    @staticmethod
    def createUser(username, password):
        if os.path.isdir(password):
            return "This user already exists!"
        else:
            os.mkdir(username)
            os.chdir(username)
            key = cryption.genarateKey(password=password, saltSize=32, loadSalt=False, saveSalt=True)
            with open("key.key", "wb") as keyFile:
                keyFile.write(key)
            with open("passwords.txt", "x"):
                return()
            