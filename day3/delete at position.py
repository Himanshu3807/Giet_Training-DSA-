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
    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("Linked list is empty. Cannot delete elements.")
        elif position == 1:
            self.deleteFromBeginning()
        else:
            temp = self.head
            count = 1
            while temp is not None:
                if count == position:
                    break
                temp=temp.next
                count=count+1
            if temp is None:
                print(" There are less than {} elements in linked list. Cannot delete elements.".format(position))
            elif temp.next is None:
                self.deleteFromLast()
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
            temp.next=None
            temp.prevoius=None
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no. of nodes:", x.length())
print("Delete from position")
x.deleteFromPosition(3)
x.printLinkedList()
