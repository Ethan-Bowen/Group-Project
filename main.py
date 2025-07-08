from password import Password
from user import User
from passwordBank import Node
from passwordBank import LinkedList
# import mainMenu

passwd = Password(12345, "Hello World")
# print(passwd.password, " ", passwd.website)

user = User("BadPassword123")
# print(user.userPassword)

node = Node(passwd)
print(node.getData().printData())
bank = LinkedList()
bank.insertFromHead(node)
password = Password(54321, "ILikeCookies.com")
nodeTwo = Node(password)
bank.insertFromHead(nodeTwo)
print(bank.returnList())

