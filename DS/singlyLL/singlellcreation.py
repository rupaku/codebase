class Node:
    def __init__(self, datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None

class LinkedList:
    def __init__(self):
        self.headvalue = None
    def print(self):
        printvalue=self.headvalue
        while printvalue is not None:
            print(printvalue.datavalue)
            printvalue= printvalue.nextvalue

x=LinkedList()
x.headvalue=Node("Rupa")
data2=Node("kumari")
data3=Node("hello")

x.headvalue.nextvalue = data2
data2.nextvalue = data3

x.print()
