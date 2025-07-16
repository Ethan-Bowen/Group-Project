class HashMap:

    def __init__(self, size):
        self.size = size
        self.hashMap = self.makeBucket()

    #sets the size of the hash map
    def makeBucket(self):
        bucket = [[] for x in range(self.size)]
        return bucket
    
    #Enters a new password into the hash map given the affiliated website and the password
    def setValue(self, key, value):
        hashKey = hash(key) % self.size
        bucket = self.hashMap[hashKey]
        keyFound = False
        for x, record in enumerate(bucket):
            recordKey = record
            if recordKey == key:
                keyFound = True
                break
        if keyFound:
            bucket[x] = (key, value)
        else:
            bucket.append((key, value))
            
    #Returns the value of the password given the website title
    def getValue(self, key):
        hashKey = hash(key) % self.size
        bucket = self.hashMap[hashKey]
        keyFound = False
        for x, record in enumerate(bucket):
            recordKey = record
            if recordKey == key:
                keyFound = True
                break
        if keyFound:
            return recordKey
        else:
            return "No password found"
        
    #Removes a password given the website title
    def removeValue(self, key):
        hashKey = hash(key) % self.size
        bucket = self.hashMap[hashKey]
        keyFound = False
        for x, record in enumerate(bucket):
            recordKey = record
            if recordKey == key:
                keyFound = True
                break
        if keyFound:
            bucket.pop(x)
        else:
            return "No password found"

    def __str__(self):
        return "".join(str(item) for item in self.hashMap)
    
    #Will read saved password information from a file and save it to the hash map
    def readSavedPasswords(self, file):
        for line in file:
            counter = 0
            for word in line.split():
                if (counter % 2) == 0:
                    website = word
                else: 
                    password = word
                counter += 1
            self.setValue(website, password)
        
    #TODO
    # def savePasswords(self, file):
        

