class HashMap:

    def __init__(self):
        self.map = {}

    #Enters a new password into the hash map given the affiliated website and the password
    def setValue(self, key, value):
        self.map.update({key : value})
            
    #Returns the value of the password given the website title
    def getValue(self, key):
        keyFound = False #If the key given is found
        for x in self.map: #Loops through all the keys in the hash
            if x == key: #If the key is found it breaks the loop
                keyFound = True
                break
        if keyFound == True:
            return self.map.get(key) #Returns the password if key is found
        else:
            return "Password not found" #Returns this if key is not found
            
    #Removes a password given the website title
    def removeValue(self, key):
        keyFound = False #If the key given is found
        for x in self.map: #Loops through all the keys in the hash
            if x == key: #If the key is found it breaks the loop
                keyFound = True
                break
        if keyFound == True:
            self.map.pop(key) #If the key is found it removes the key and password from the hash
        else:
            return "Password not found" #If key is not found it returns this

    #Will read saved password information from a file and save it to the hash map
    def readSavedPasswords(self, filename):
        with open(filename, "r") as file: #Opens a file using filename
            password = None
            website = None
            for line in file: #Loops through lines in the file
                counter = 0 #Iteration counter
                for word in line.split(): #Loops through each word in the line
                    if (counter % 2) == 0: #If counter % 2 is 0 then the word is a website
                        website = word
                    else: 
                        password = word #If counter % 2 is not 0 then it is a password
                    counter += 1 
                self.setValue(website, password) #At the end of the line the hash map adds the password and website to the hash

    #Saves the current contents of the hash map to a file
    def savePasswords(self, filename):
        with open(filename, "w") as file: #Opens the file with filename
            for key in self.map: #Loops through each key in the hash
                file.write(key + " "  + self.map.get(key) + "\n") #Writes both the website and password to the file

