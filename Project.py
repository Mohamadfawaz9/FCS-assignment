def employee():
    s = '''
    Hello! Please enter:
    1. To go to the drivers' menu
    2. To go to the cities' menu
    3. To exit the system
    '''
    print(s)
    entry = int(input("Enter one of the options(1, 2 or 3): "))
    while entry == 1 or entry == 2 or entry == 3:
        if entry == 1:
            pass
        elif entry == 2:
            pass
        elif entry == 3:
            pass
class Node:
    def __init__(self,info,next):
        self.info = info
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addtohead(self,info):
        n = Node(info,None)
        if self.size == 0:
            self.head = n
            self.tail = n
            self.size = 1
        else:
            n.head = self.head
            self.head = n
            self.size += 1

    def addtotail(self,info):
        n = Node(info,None)
        if self.size == 0:
            return self.addtohead(info)
        else:
            self.tail.next = n
            self.tail = n
            self.size += 1

    def deletehead(self):
        if self.size == 0:
            return
        elif self.size == 1:
            val = self.head.info
            self.head = None
            self.tail = None
            self.size = 0
            return val
        else:
            val = self.head.info
            self.head = self.head.next
            self.size -=1
            return val

    def deletetail(self):
        if self.size <= 1:
            return self.deletehead
        else:
            val = self.tail.info
            i = self.head
            while i.next.next != None:
                i = i.next
            self.tail = i
            self.tail.next = None
            return val

    def printLL(self,info):
        i = self.head
        while i != None:
            print(i.info,"->",end = "")
            i = i.next
        print()