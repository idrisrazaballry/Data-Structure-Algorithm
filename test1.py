# WAP to implement queue data structure using 2 stacks

class stack:
    def __init__(self):
        self.s1 = []

    def push(self, val):
        self.s1.append(val)

    def pop(self):
        if len(self.s1) == 0:
            return False
        else:
            return self.s1.pop()

    def display(self):
        print(self.s1)

class queue:
    def __init__(self):
        self.Instack = stack()
        self.OutStack = stack()
    
    def enqueue(self, val):
        self.Instack.push(val)
    
    def dequeue(self):
        while len(self.Instack.s1) != 0:
            self.OutStack.push(self.Instack.pop())
        res = self.OutStack.pop()
        while len(self.OutStack.s1) != 0:
            self.Instack.push(self.OutStack.pop())
        return res
    
    def display(self):
        if len(self.Instack.s1) !=0:
            print(self.Instack.s1)
        else:
            print("No stack elements in the stack")

    def peek(self):
        pass

q1=queue()
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.display()
q1.dequeue()
q1.display()
