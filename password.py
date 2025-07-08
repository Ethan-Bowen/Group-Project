class Password:

    def __init__(self, password, website):
        self.password = password
        self.website = website

    def getPassword(self):
        return self.password
    
    def setPassword(self, input):
        self.password = input

    def delPassword(self):
        del self.password
    
    def getWebsite(self):
        return self.website
    
    def setWebsite(self, input):
        self.website = input

    def delWebsite(self):
        del self.website
    
