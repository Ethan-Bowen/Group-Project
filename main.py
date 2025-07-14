from password import Password
from passwordBank import HashMap
from user import User
# import mainMenu

passwd = Password(12345, "Hello World")
print(passwd.password, " ", passwd.website)

user = User("BadPassword123")
print(user.userPassword)

hashMap = HashMap(10)
hashMap.setValue('hello', 'world')
print(hashMap)
print()
hashMap.setValue('hello', 'newWorld')
print(hashMap)
print()

hashMap.setValue(passwd.website, passwd.password)
print(hashMap)
print()
print(hashMap)
print()
print(hashMap.getValue("Hello World"))
print()
hashMap.removeValue("Hello World")
print()
print(hashMap)