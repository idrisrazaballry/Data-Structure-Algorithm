class node:
    def __init__(self, data):
        self.pre = None
        self.data = data
        self.next = None

class circularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_last(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.pre = newNode
            # break
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newNode.pre = temp
            temp.next = newNode
            newNode.next = self.head
            self.head.pre = newNode

    def display(self):
        if self.head is None:
            print("No node to display in double LL")
        else:
            temp=self.head
            while temp:
                print(temp.data, end=' <==> ')
                temp=temp.next
                if temp == self.head:
                    break
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
                if temp == self.head:
                    break
            return cnt
    
    def insert_at_first(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            newNode.pre = newNode
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head.pre = newNode
            newNode.pre = temp
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
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
            self.head.pre = temp

    def delete_at_first(self):
        if self.head is None:
            print("No node to delete")
        elif self.length() == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head.next.pre = temp
            self.head = self.head.next

cll = circularDoubleLinkedList()
# cll.display()
cll.insert_at_last(23)
cll.insert_at_last(2)
cll.insert_at_last(12)
cll.insert_at_last(9)
cll.display()