from password import Password
from user import User
#from passwordBank import PasswordBank
import mainMenu

passwd = Password(12345, "Hello World")
print(passwd.password, " ", passwd.website)

user = User("BadPassword123")
print(user.userPassword)
