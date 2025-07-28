class HashMap:

    def __init__(self):
        self.map = {}

    #Enters a new password into the hash map given the affiliated website and the password
    def setValue(self, key, value):
        self.map.update({key : value})
            
    #Returns the value of the password given the website title
    def getValue(self, key):
        keyFound = False
        for x in self.map:
            if x == key:
                keyFound = True
                break
        if keyFound == True:
            return self.map.get(key)
        else:
            return "Password not found"
            
    #Removes a password given the website title
    def removeValue(self, key):
        keyFound = False
        for x in self.map:
            if x == key:
                keyFound = True
                break
        if keyFound == True:
            self.map.pop(key)
        else:
            return "Password not found"

    #Will read saved password information from a file and save it to the hash map
    def readSavedPasswords(self, filename):
        with open(filename, "r") as file:
            for line in file:
                counter = 0
                for word in line.split():
                    if (counter % 2) == 0:
                        website = word
                    else: 
                        password = word
                    counter += 1
                self.setValue(website, password)

    #Saves the current contents of the hash map to a file
    def savePasswords(self, filename):
        for key in self.map:
            with open(filename, "w") as file:
                file.write(key + " "  + self.map.get(key) + "\n")

