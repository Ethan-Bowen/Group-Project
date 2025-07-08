from password import Password

#Node class for a linked list
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

#returns data of node
    def getData(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None

#inserts new node at the head of the list
    def insertFromHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    
#insterts new node at the tail of the list
    def insertFromTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        index = self.head
        while(index.next):
            index = index.next
        index.next = newNode

#Returns each element of the list starting at the head
    def returnList(self):
        if self.head is None:
            return
        index = self.head
        while(index.next):
                index.data
                index = index.next