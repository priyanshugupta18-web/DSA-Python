# Doubly LinkedList and Circular LinkedList

class node:
    def __init__(self, value):
        self.info = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head
        if (self.head != None):
            self.head = node(self.head)
    
    def insertAtEnd(self, value):
        new_node = node(value)
        temp = self.head
        if self.head is not None:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insertAtBeg(self, value):
        new_node = node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
    
    def insertInMid(self, value, insAft):
        new_node = node(value)
        temp = self.head
        if self.head is not None:
            while temp.next is not None:
                if temp.info is insAft:
                    new_node.next = temp.next
                    temp.next.prev = new_node
                    temp.next = new_node
                    new_node.prev = temp
                    return
                temp = temp.next
        else:
            raise ValueError("Cannot insert in the middle of an empty linked list")
    
    def Delete(self, value):
        temp = self.head
        if self.head is not None:
            if temp.info == value:
               if temp.next is not None:
                    self.head = temp.next 
                    self.head.prev = None
                    return
               else:
                   self.head = None
                   return                   
            while temp.next is not None:
                if temp.info == value:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
                temp = temp.next
            if temp.info == value:
                temp.prev.next = None
        else:
            raise ValueError("Cannot Delete anything from an empty linked list")

    def printDLL(self):
        temp = self.head
        while temp.next is not None:
            print(temp.info, end = " <--> ")
            temp = temp.next
        print(temp.info)
            
DLL1 = DoublyLinkedList()
DLL1.insertAtEnd(23)
DLL1.insertAtEnd(25)
DLL1.insertAtEnd(34)
DLL1.insertAtEnd(43)
DLL1.insertAtBeg(5)
DLL1.insertInMid(14, 5)
DLL1.Delete(5)
DLL1.printDLL()
