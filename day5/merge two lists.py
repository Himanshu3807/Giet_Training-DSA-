#Join two linked List
#list1 = 1,2,4,3,5
#list2 = 9,8,11
#n = 2
#o/p = 1,2,9,8,11,4,3,5
class Node:
    def _init_(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data,end=" ")
            printval = printval.next
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def merge(self,n,list3):
        temp = self.head

        while temp is not None:
            if (n ==0):
                list3.listprint()
                n-=1
            else:
                print(temp.data)
                temp = temp.next
                n -= 1

list1 = LinkedList()
list2 = LinkedList()
list(map(list1.insert,input().split()))
list(map(list2.insert,input().split()))
n = int(input())
list1.merge(n,list2)
