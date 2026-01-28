class node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        if(head != None):
            self.head = node(head)
        else:
            self.head = None
    
    def insertAtEnd(self, value):
        new_node = node(value)
        if(self.head != None):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node
    
    def printl(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)

    def insertAtBeg(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

    def insertAtMid(self, value, insertAft):
        new_node = node(value)
        temp = self.head
        while(temp.next != None):
            if (temp.data == insertAft):
                new_node.next = temp.next
                temp.next = new_node
                break
            else:
                temp = temp.next
        
    def deletel(self, value):
        if (self.head.data == value):
            self.head = self.head.next

        else:
            temp = self.head
            prev = self.head

            while (temp.next != None):
                if (temp.data == value):
                    prev.next = temp.next
                    break
                else:
                    prev = temp
                    temp = temp.next
            if (temp.data == value):
                prev.next = None

l1 = SinglyLinkedList()
l1.insertAtEnd(25)
l1.insertAtEnd(35)
l1.insertAtEnd(45)
l1.insertAtBeg(15)
l1.insertAtMid(30, 25)
l1.deletel(45)
l1.printl()

