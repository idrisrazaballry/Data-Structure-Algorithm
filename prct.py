''' Implementation of stack without limited size '''
# class st1:
#     def __init__(self):
#         self.s1=[]
    
#     def push(self, val):
#         self.s1.append(val)
    
#     def pop(self):
#         self.s1.pop()
    
#     def display(self):
#         if len(self.s1)!=0:
#             for i in range(len(self.s1)-1, -1, -1):
#                 print(self.s1[i])
#         else:
#             print("No elements in stack")
    
#     def peek(self):
#         print(self.s1[-1])

# s1=st1()
# s1.push(3)
# s1.display()
# print()
# print()
# print()
# s1.push(4)
# s1.push(5)
# s1.push(7)
# s1.push(8)
# s1.display()
# print()
# print()
# print()
# s1.pop()
# s1.pop()
# s1.pop()
# s1.display()


''' Implementation of stack with limited size '''

class STACK:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.s1=[]

    def isFull(self):
        if len(self.s1)==self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if len(self.s1)==0:
            return True
        else:
            return False
        
    def push(self, val):
        if self.isFull():
            print("The stack is full")
        else:
            self.s1.append(val)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.s1.pop()
    
    def display(self):
        if self.isEmpty():
            print("No elements in the stack")
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
    
    def peek(self):
        if self.isEmpty():
            print("No elemenst in the stack:")
        else:
            print(self.s1[-1])

s1=STACK(4)
while True:
    print(" ----- Stack Operations -----\n")
    print("1. Push\n  2. Pop\n 3. Display\n 4. Peek\n 5. IsFull\n 6. IsEmpty\n 7. Exit\n")
    opt=int(input("Enter the option:\n"))
    match opt:
        case 1:
            val=input("Enter the value: ")
            s1.push(val)
        case 2:
            s1.pop()
        case 3:
            s1.display()
        case 4:
            s1.peek()
        case 5:
            print("Is stack full: ", s1.IsFull())
        case 6:
            print("Is Stack empty: ", s1.IsEmpty())
        case 7:
            print("--- Exiting Programm ---")
            break
        case _:
            print("In valid option")