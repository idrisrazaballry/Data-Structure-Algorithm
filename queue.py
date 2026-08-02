class QUEUE:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.q1=[]

    def IsFull(self):
        if len(self.q1)==self.maxSize:
            return True
        else:
            return False
        
    def IsEmpty(self):
        if len(self.q1)==0:
            return True
        else:
            return False
        
    def enqueue(self, val):
        if self.IsFull():
            print("Queue is full")
        else:
            self.q1.append(val)

    def display(self):
        if self.IsEmpty():
            print("No elements in queue")
        else:
            print(self.q1)

    def dequeue(self):
        if self.IsEmpty():
            print("No elements to remove")
        else:
            self.q1.pop(0)

    def peek(self):
        if self.IsEmpty():
            print("No elements to peek")
        else:
            print("Top elements is:", self.q1[0])

q1=QUEUE(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.display()
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.display()