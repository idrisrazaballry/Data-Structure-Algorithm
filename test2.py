# WAP to reverse the given string using stack implementation

# class stack:
#     def __init__(self):
#         self.s1 = []

#     def push(self, val):
#         self.s1.append(val)
    
#     def pop(self):
#         if len(self.s1) == 0:
#             return False
#         else:
#             return self.s1.pop()

# s = stack()
# str = input("Enter the string: ")
# print("Given string --> ", str)
# for i in range(len(str)):
#     s.push(str[i])

# print()

# res = ""
# while (len(s.s1)) != 0:
#     res += s.pop()
# print("Reversed string --> ",res)


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
