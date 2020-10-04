class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None   
        self.tail = None
        self.length = 0
    
    def printList(self):
        curNode = self.head
        while(curNode):
            print(curNode.data,end=" ")
            curNode = curNode.next
    
    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode    
        self.length +=1

    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode    
    
    def insert_after_node(self,prevNode,data):
        if not prevNode:
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode    
    
    def insertAfterNode(self,pos,data):
        
        if pos == 0:
           self.prepend(data)
           return
        
        currentNode = self.head    
        prevNode = None
        count = 0
        while currentNode and count != pos:
            prevNode = currentNode
            currentNode = currentNode.next
            count += 1 
        if currentNode is None:
            return
        newNode = Node(data)
        tmp = prevNode.next         
        prevNode.next = newNode
        newNode.next = tmp

    

    def delete(self,key):
        currentNode = self.head
        if currentNode and currentNode.data == key:
            self.head = currentNode.next
            currentNode = None
            return
        prevNode = None
        while currentNode and currentNode.data != key:
            prevNode = currentNode
            currentNode = currentNode.next
        if currentNode is None:
            return
        else:
            prevNode.next = currentNode.next 
            currentNode = None

    def delete_node_at_pos(self,pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prevNode = None
        count = 1
        while cur_node and count != pos:
            prevNode = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prevNode.next = cur_node.next
        cur_node = None               

    def reverserList(self):
        prevNode = None
        curNode = self.head
        while curNode:
            nxt = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nxt
        self.head = prevNode

llist = SinglyLinkedList()   
llist.append("A") 
llist.append("B")    
llist.append("C") 
llist.append("D")   
# llist.printList()
llist.delete("C")
#llist.insertAfterNode(0,"A")
llist.reverserList()
llist.printList()