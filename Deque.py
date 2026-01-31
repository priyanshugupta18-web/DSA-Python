class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (len(self.items) == 0)

    def insertAtBeg(self, value):
        self.items.insert(0, value)
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteFromBeg(self):
        if (len(self.items) == 0):
            raise Exception("Dequeue is Empty")
        else:
            return self.items.pop(0)
        
    def deleteFromEnd(self):
        if (len(self.items) == 0):
            raise Exception("Dequeue is Empty")
        else:
            return self.items.pop()
        
q = Deque()

q.insertAtBeg(10)
q.insertAtBeg(20)
q.insertAtEnd(30)
q.insertAtEnd(40)
print(q.deleteFromBeg())
print(q.deleteFromEnd())
print(q.isEmpty())