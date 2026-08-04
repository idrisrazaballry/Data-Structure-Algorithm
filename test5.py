''' Alex is tried to arrange his text books in a book shelf, that shelf able to take 
    only limited number of books then immediately arrange his books in a new shelf 
    automatically.

    Now consider arrangement of books in a stack if one stack is reached maximum size
    immediately create new stack and push the books to newly created stack
 '''

class StackInstack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
    
    def push(self, val):
        if len(self.stack) > 0 and len(self.stack[-1]) < self.maxSize:
            self.stack[-1].append(val)
        else:
            self.stack.append([val])

    def display(self):
        print(self.stack)

    def pop(self):
        if self.stack == None:
            print("No elements in the stack")
        else:
            self.stack[-1].pop()
    
    def popAt(self,stackNum):
        if stackNum > 0 and stackNum < len(self.stack):
            self.stack[stackNum - 1].pop()
        else:
            print("Stack number doesn't exists")
    
    def pushAt(self,stackNum, val):
        if stackNum > 0 and stackNum < len(self.stack):
            if len(self.stack[stackNum - 1]) == self.maxSize:
                print("Stack is full")
            else:
                self.stack[stackNum - 1].append(val)
        else:
            print("Stack number doesn't exists")

    def peek(self):
        if self.stack == None:
            print("No elements in the stack")
        else:
            print(self.stack[-1])

    def peekAt(self):
        pass

stk = StackInstack(4)
stk.push("math")
stk.push("science")
stk.push("socila science")
stk.push("m1")
stk.push("m2")
stk.push("m3")
stk.push("OS")
stk.display()
print()
stk.push("Web")
stk.push("HTML")
stk.push("CSS")
stk.push("JS")
stk.display()
print()
stk.pop()
stk.display()
print()
stk.popAt(2)
stk.display()
stk.popAt(4)
stk.display()

