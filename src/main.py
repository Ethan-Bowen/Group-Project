from password import Password
from passwordBank import HashMap
from user import User
import os
# import mainMenu

# passwd = Password(12345, "Hello World")
# print(passwd.password, " ", passwd.website)

# user = User("BadPassword123")
# print(user.userPassword)

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

def main():
    
    return

user = User("Username", "12345")
user.createUser(user.username, user.password)
hash = HashMap(10)
os.chdir(user.username)
file = open("passwords.txt")
hash.readSavedPasswords(file)
file.close()
print(hash)