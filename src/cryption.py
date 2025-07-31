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

#Genarates the encryption key using the given password and salt
@staticmethod
def genarateKey(password, saltSize = 32, loadSalt = False, saveSalt = True):
    if loadSalt: #Checks if load salt is true. If it is it loads the salt from a file
        with open("salt.salt", "rb") as saltFile:
            salt = saltFile.read()
    elif saveSalt: #If save salt is true then it will save the current salt to the salt file
        salt = createSalt(saltSize)
        with open("salt.salt", "wb") as saltFile:
            saltFile.write(salt)
    key = deriveKey(salt, password) #Uses the deriveKey fn to create a key
    return base64.urlsafe_b64encode(key) #Returns the encryption key

#Encrypts the given file with the given key
@staticmethod
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file: #Opens and reads the decrypted file
        fileData = file.read()
    encryptedData = f.encrypt(fileData) #Encrypts the file data with the key and writes it to the file
    with open(filename, "wb") as file:
        file.write(encryptedData)

#Decrypts the given file given correct key, else returns invalid password
@staticmethod
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file: #Opens and reads encrypted data
        encryptedData = file.read()
    decryptedData = f.decrypt(encryptedData) #Attempts to decrypt data
    with open(filename, "wb") as file: #Saves decrypted data to the file
        file.write(decryptedData)