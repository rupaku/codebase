class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printvalue(self):
        printv=self.head
        while printv is not None:
            print(printv.data)
            printv=printv.next
    def beginning(self,data4):
        newvalue=Node(data4)
        newvalue.next=self.head
        self.head=newvalue
    def end(self,data5):
        newvalue=Node(data5)
        if self.head is None:
            self.head=newvalue
            return
        lastnode=self.head
        while(lastnode.next):
            lastnode = lastnode.next
        lastnode.next=newvalue

x=LinkedList()
x.head=Node("Rupa")
data2=Node("kumari")
x.head.next=data2
x.beginning("welcome")
x.end("bbyee")
x.printvalue()