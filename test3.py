# WAP to create a single linked list inside a stack DS

class node:
    def __init__(self, data):
        self.data = data
        self.addr = None

class stack_linked_list:
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.addr = self.head
            self.head = newNode
    
    def display(self):
        if self.head is None:
            print("No nodes to display")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.addr
            print()
    
    def peek(self):
        if self.head is None:
            print("No elements to peek")
        else:
            print(self.head.data)

