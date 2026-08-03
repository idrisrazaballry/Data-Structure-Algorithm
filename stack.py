# Implementation of stack without any limited size

# class STACK:
#     def __init__(self):
#         self.s1 = []

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

# st1=STACK()
# st1.push(10)
# st1.display()
# st1.peek()
# st1.pop()
# st1.display()


''' Implementation of stack with limited size '''

class STACK:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.s1=[]

    def IsFull(self):
        if len(self.s1)==self.maxSize:
            return True
        else:
            return False
        
    def IsEmpty(self):
        if len(self.s1)==0:
            return True
        else:
            return False
    
    def push(self, val):
        if self.IsFull():
            print("Stack is full")
        else:
            self.s1.append(val)
    
    def display(self):
        if self.IsEmpty():
            print("No elements in stack")
        else:
            for i in range(len(self.s1)-1, -1,-1):
                print(self.s1[i])

    def peek(self):
        if self.IsEmpty():
            print("No elements to peek")
        else:
            print("Top element is: ", self.s1[-1])

    def pop(self):
        if self.IsEmpty():
            print("No elements to remove ")
        else:
            self.s1.pop()

st1=STACK(3)
while True:
    print("------------ STACK OPERATIONS --------------")
    print(" 1. Push\n 2. Pop\n 3. Display\n 4. Peek\n 5. Is Full\n 6. Is Emply\n 7. Exit")
    opt=int(input("Enter the options: "))
    match opt:
        case 1:
            val=input("Enter the value: ")
            st1.push(val)
        case 2:
            st1.pop()
        case 3:
            st1.display()
        case 4:
            st1.peek()
        case 5:
            print("Is stack full: ", st1.IsFull())
        case 6:
            print("Is Stack empty: ", st1.IsEmpty())
        case 7:
            print("--- Exiting Programm ---")
            break
        case _:
            print("In valid option")
