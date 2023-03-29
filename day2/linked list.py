class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None

    def listprint(self):
        printval=self.head
        while(printval is not None):
            print(printval.data)
            printval=printval.next
 
    def atBeginning(self,newdata):
        Newdata=Node(newdata)
        Newdata.next=self.head
        self.head=Newdata

    def atEnd(self,newdata):
        Newdata=Node(newdata)
        if self.head==None:
            self.head=Newdata
            return
        current=self.head
        while(current.next is not None):
            current=current.next
        else:
            current.next=Newdata

    def atPosition(self,position,newdata):
        Newdata=Node(newdata)
        if position==0:
            self.atBeginning()
        else:
            count=0
            current=self.head
            while(current.next is not None):
                count+=1
                if count==position-1:
                    next=current.next
                    current.next=Newdata
                    Newdata.next=next
                    return
                current=current.next

    def del_start(self):
        if self.head==None:
            return 0
        else:
            self.head=self.head.next

    def del_end(self):
        if self.head==None:
            print("No Element")
            return
        if self.head.next==None:
            self.head=None
            return
        sec_last=self.head
        while sec_last.next.next is not None:
            sec_last=sec_last.next
        sec_last.next=None

    def del_value(self,data):
        if self.head==None:
            print("No Element")
            return
        if self.head.data==data:
            self.head=None
            return
        current=self.head
        while(current.next is not None):
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
        
List=SLinkedList()
List.head=Node("A")
e1=Node("B")
e2=Node("C")
List.head.next=e1
e1.next=e2
List.listprint()
List.atBeginning("#")
List.listprint()
List.atEnd("|")
List.listprint()
print("--------------------")
List.atPosition(3,"XY")
List.listprint()
print("--------------------")
List.del_start()
List.listprint()
print("--------------------")
List.del_end()
List.listprint()
print("--------------------")
List.del_value("XY")
List.listprint()
