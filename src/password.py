class Password:
#Honnestly might be redendant but I'm keeping it around in case I need it
    def __init__(self, website, password):
        self.password = password
        self.website = website
    
    def __str__(self):
        string = str((str(self.website), str(self.password)))
        return string
