class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.insert(0, value)
    
    def peek(self):
        if (len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return self.s[0]
        
    def pop(self):
        if (len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return self.s.pop(0)
        
    def isEmpty(self):
        if (len(self.s) == 0):
            return True
        return False
    
s1 = stack()
s1.push(13)
s1.push(3)
s1.push(16)
print(s1.peek())
print(s1.pop())
print(s1.isEmpty())
