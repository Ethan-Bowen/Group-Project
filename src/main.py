from password import Password
from passwordBank import HashMap
from user import User
import os
import cryption
from login import UserCreatorGUI
import tkinter as tk

# passwd = Password(12345, "Hello World")
# print(passwd.password, " ", passwd.website)

# user = User("Username", "BadPassword123")
# user.createUser()

# hashMap = HashMap(10)
# hashMap.setValue('hello', 'world')
# print(hashMap)
# print()
# hashMap.setValue('hello', 'newWorld')
# print(hashMap)
# print()

# hashMap.setValue(passwd.website, passwd.password)
# print(hashMap)
# print()
# print(hashMap)
# print()
# print(hashMap.getValue("Hello World"))
# print()
# hashMap.removeValue("Hello World")
# print()
# print(hashMap)

# map = HashMap()
# map.setValue("website", "password")
# print(map.map)
# map.setValue("hello", "world")
# print(map.map)
# map.setValue("website", "1234")
# print(map.map)
# print(map.getValue("hello"))
# map.removeValue("hello")
# print(map.map)
# print()
# os.chdir("Username")
# file = open("passwords.txt")
# map.readSavedPasswords(file)
# print(map.map)
# fileTwo = open("passwordTwo.txt", "wt")
# map.savePasswords(fileTwo)
# file.close()
# fileTwo.close()

# def main():

#     return

if __name__ == "__main__":
    root = tk.Tk()
    app = UserCreatorGUI(root)
    app.root.mainloop()