class Password:

    def __init__(self, password, website):
        self.password = password
        self.website = website
    
    def __str__(self):
        string = str((str(self.website), str(self.password)))
        return string
