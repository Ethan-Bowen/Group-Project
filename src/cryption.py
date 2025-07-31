from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64

#Creates salt for the hash
#Default size is 32 but can be changed
#Don"t make size smaller than 32
@staticmethod
def createSalt(size=32):
    return secrets.token_bytes(size)

#Derives the password with the salt
@staticmethod
def deriveKey(salt, password):
    kdf = Scrypt(salt, 32, 2**14, 8, 1)
    return kdf.derive(password.encode())

#Returns the contents of the salt.salt file
@staticmethod
def loadSalt():
    return open("salt.salt", "rb").read()

#Genarates the encryption key using
@staticmethod
def genarateKey(password, saltSize = 32, loadSalt = False, saveSalt = True):
    if loadSalt:
        with open("salt.salt", "rb") as saltFile:
            salt = saltFile.read()
    elif saveSalt:
        salt = createSalt(saltSize)
        with open("salt.salt", "wb") as saltFile:
            saltFile.write(salt)
    key = deriveKey(salt, password)
    return base64.urlsafe_b64encode(key)

#Encrypts the given file with the given key
@staticmethod
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        fileData = file.read()
    encryptedData = f.encrypt(fileData)
    with open(filename, "wb") as file:
        file.write(encryptedData)

#Decrypts the given file given correct key, else returns invalid password
@staticmethod
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encryptedData = file.read()
    decryptedData = f.decrypt(encryptedData)
    with open(filename, "wb") as file:
        file.write(decryptedData)