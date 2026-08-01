class node:
    def __init__(self, data):
        self.pre = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_last(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            newNode.prev = temp
            temp.next = newNode
        

    def display(self):
        if self.head is None:
            print("No node to display in double LL")
        else:
            temp=self.head
            while temp:
                print(temp.data, end=' <==> ')
                temp=temp.next
            print()

    def length(self):
        if self.head is None:
            print("NO node to count in double LL")
        else:
            temp = self.head
            cnt = 0
            while temp:
                cnt += 1
                temp = temp.next
            return cnt

    def insert_at_first(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.pre = newNode
            self.head = newNode

    def insert_at_loc(self, loc, val):
        newNode = node(val)
        if loc <= 0:
            print("Enter loc above 0")
        elif loc == 1:
            self.insert_at_first(val)
        elif loc == self.length() + 1:
            self.insert_at_last(val)
        elif loc > self.length():
            print("Enter the loc less than :", self.length())
        else:
            temp = self.head
            cnt = 1
            while temp.next != None and cnt < loc-1:
                temp = temp.next
                cnt += 1
            newNode.next = temp.next
            temp.next.pre = newNode
            newNode.pre = temp
            temp.next = newNode

    def delete_at_last(self):
        if self.head is None:
            print("No node to delete")
        elif self.length() == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    def delete_at_first(self):
        if self.head is None:
            print("No nodes to delete")
        elif self.length() == 1:
            self.head = None
        else:
            self.head=self.head.next

    def delete_at_loc(self, loc):
        if loc <= 0:
            print("Enter the location above 0")
        elif loc == 1:
            self.delete_at_first()
        elif loc < self.length():
            print("Enter the location less than --> ", self.length())
        elif loc == self.length():
            self.delete_at_last()
        else:
            temp = self.head()
            cnt = 1
            while temp.next != None and cnt < loc-1:
                temp = temp.next
                cnt += 1
            temp.next.next.prev = temp
            temp.next = temp.next.next


d = doubleLinkedList()
d.display()
d.length()
d.insert_at_last(3)
d.insert_at_last(5)
d.insert_at_last(8)
d.insert_at_last(2)
d.insert_at_last(1)
print("total nodes ->",d.length())
d.display()
d.insert_at_loc(2, "AC")
d.display()
d.delete_at_last()
d.display()
print("total nodes ->",d.length())
d.delete_at_last()
d.display()
print("total nodes ->",d.length())
print()
d.delete_at_first()
d.display()
print("total nodes ->",d.length())
print()
d.delete_at_first()
d.display()
print("total nodes ->",d.length())
print()
d.delete_at_last()
d.display()
print("total nodes ->",d.length())