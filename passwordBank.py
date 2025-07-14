class HashMap:

    def __init__(self, size):
        self.size = size
        self.hashMap = self.makeBucket()

    def makeBucket(self):
        bucket = [[] for x in range(self.size)]
        return bucket
    
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
            return None
        else:
            return "No password found"

    def __str__(self):
        return "".join(str(item) for item in self.hashMap)
