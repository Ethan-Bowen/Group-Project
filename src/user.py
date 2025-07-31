import os
from passwordBank import HashMap
import cryption

class User:

    #Used to create a folder and txt file for a new user
    @staticmethod
    def createUser(username, password):
        if os.path.isdir(password): #Checks if a folder with the Username already exists
            return "This user already exists!" #Returns this if the user exists
        else: #If not then the user folder is created as well as the passwords.txt, salt.salt, and key.key files 
            os.mkdir(username) #Makes user folder
            os.chdir(username) #Moves to user folder
            key = cryption.genarateKey(password=password, saltSize=32, loadSalt=False, saveSalt=True) #Creates encryption key and saves it to a file
            with open("key.key", "wb") as keyFile:
                keyFile.write(key)
            with open("passwords.txt", "x"): #Makes passwords.txt
                return()
            