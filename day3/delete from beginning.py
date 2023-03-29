class Node:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
    
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def deleteFromBeginning(self):
            if self.isEmpty():
                print("Linked List is empty. Cannot delete element")
            elif self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.previous = None
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no. of nodes:", x.length())
print("Delete at the begining")
x.deleteFromBeginning()
x.printLinkedList()
