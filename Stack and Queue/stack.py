class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []    

    def topElement(self):
        if not self.isEmpty():
            return self.items[-1]    

    def getStack(self):
        return self.items

s = Stack()
print(s.isEmpty())
s.push("A")            
s.push("B")            
s.push("C")            
print(s.isEmpty())
# s.pop()
print(s.getStack())