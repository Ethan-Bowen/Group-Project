class User:

    def __init__(self, userPassword):
        self.userPassword = userPassword
    
    def getUserPassword(self):
        return self.userPassword
    
    def setUserPassword(self, input):
        self.userPassword = input
    
    def delUserPassword(self):
        del self.userPassword
