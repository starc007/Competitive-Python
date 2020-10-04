class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None        
    
    def insert(self,value):
        if self.root is None:
               self.root = Node(value)
        else:
            self.insertNode(value,self.root)

    def insertNode(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self.insertNode(value,currentNode.left)
        elif value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self.insertNode(value, currentNode.right)
        else: 
            print("Value is already present")                       

    def find(self,value):
        if self.root:
            isFound = self.findValue(value, self.root)
            if isFound:
                return True
            return False
        else:
            return None

    def findValue(self,value, currentNode):
        if value > currentNode.value and currentNode.right:
            return self.findValue(value, currentNode.right)
        elif value < currentNode.value and currentNode.left:
            return self.findValue(value,currentNode.left)
        if value == currentNode.value:
            return True        

    def BFS(self):
        if self.root is None:
            return
        data = []
        queue = []
        node = self.root
        queue.append(node)
        while (len(queue)):
            node = queue.pop(0)
            data.append(node.value)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return data

    def DFSpreOrder(self):
        data = []
        def traverse(node):
            data.append(node.value)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        traverse(self.root)
        return data    

    def DFSpostOrder(self):
        data = []
        def traverse(node):
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            data.append(node.value)
        traverse(self.root)
        return data 
    def DFSinOrder(self):
        data = []
        def traverse(node):
            if node.left: traverse(node.left)
            data.append(node.value)
            if node.right: traverse(node.right)
        traverse(self.root)
        return data 


bst = BinarySearchTree()
bst.insert(10)            
bst.insert(6)            
bst.insert(15)            
bst.insert(3)            
bst.insert(8)
bst.insert(20)
print(bst.DFSpreOrder())
print(bst.DFSpostOrder())
print(bst.DFSinOrder())
