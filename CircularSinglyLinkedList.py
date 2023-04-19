 
class Node:
     
    def __init__(self,value):
        self.value = value
        self.next = None
         
class Csll:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        
        while node:
            yield node
            node = node.next
            if node == self.head:
                break
            
    def insertCsll(self,value,location):
        if self.head is None:
            print("Csll is empty creating one with value passed!")
            node = Node(value)
            self.head = node
            self.tail = node
            node.next = node
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif location == -1:
                self.tail.next = node
                self.tail = node
                node.next = self.head
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index+=1
                node.next = tempnode.next
                tempnode.next = node
                if tempnode == self.tail:
                    self.tail = node
    
    def traverse(self):
        if self.head is None:
            print('no elements to print')
            return
        node = self.head
        
        while node:
            print(node.value)
            node = node.next
            if node == self.head:
                break
            
        print(self.head.value,self.tail.value)
        
    def searchCsll(self,value):
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return node.value, index
            node = node.next
            index+=1
            if node == self.head:
                return 'element not found'
                break
            
    def delCsll(self,location):
        if self.head is None:
            print('No elements to delete')
        else:
            node = self.head
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    node.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    node.next = None
                else:
                    while node.next != self.tail:
                        node = node.next
                        
                    node.next = self.tail.next
                    self.tail = node
            else:
                index = 0
                while index < location - 1:
                    node = node.next
                    index+=1
        
                if node.next == self.tail:
                    self.tail = node
                node.next = node.next.next
        
    def delEntireCsll(self):
        self.head = None
        self.tail.next = None
        self.tail = None
                
                    
csll = Csll()
csll.insertCsll(0,0)
csll.insertCsll(1,1)
csll.insertCsll(2,2)
csll.insertCsll(3,3)
csll.insertCsll(4,4)
csll.insertCsll(5,5)

print([a.value for a in csll])

csll.traverse()
print(csll.searchCsll(6))

csll.delCsll(5)
print([a.value for a in csll])  
csll.traverse()

csll.delEntireCsll()
print([a.value for a in csll])  
csll.traverse()

            
                