class Circular_Queue:
    # FIXED: Removed the unused 'char' parameter to prevent initialization error
    def __init__(self, maxSize): 
        self.maxSize = maxSize 
        self.cq = [None] * maxSize 
        self.front = -1 
        self.rear = -1 

    def IsFull(self):
        if self.front == 0 and self.rear + 1 == self.maxSize: 
            return True
        elif self.rear + 1 == self.front: 
            return True
        else: 
            return False

    def enqueue(self, val):
        if self.IsFull():
            print("Circular queue is full")
        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear += 1
            if self.front == -1:
                self.front = 0
            self.cq[self.rear] = val

    def IsEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def dequeue(self):
        if self.IsEmpty():
            print("NO elements in circular queue")
        else:
            idx = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front = 0
            else:
                self.front += 1  # FIXED: Changed 'self.fron' to 'self.front'
            self.cq[idx] = None

    def display(self):
        print(self.cq)

    def peek(self):
        if self.IsEmpty():
            print('C queue is empty')
        else:
            print("Peek element is :", self.cq[self.front])

    def shift_char_by_shift(self, target_char, shift):
        if self.IsEmpty():
            print("Queue is empty.")
            return 

        current = self.front
        while True:
            if self.cq[current] == target_char:
                # FIXED: Added protection so ord() doesn't crash on long words like 'Python'
                if isinstance(target_char, str) and len(target_char) == 1:
                    shifted_ascii = ord(target_char) + shift
                    self.cq[current] = chr(shifted_ascii)
                    print(f"Character '{target_char}' shifted by {shift} to '{self.cq[current]}'")
                else:
                    print(f"Cannot shift '{target_char}' because it is not a single character.")
                return 

            if current == self.rear:
                break
            current = (current + 1) % self.maxSize
        print(f"Character '{target_char}' not found in the queue.")


# --- Your Test Execution Script ---
c1 = Circular_Queue(5)  # Works perfectly now
c1.enqueue(1)
c1.enqueue('A')
c1.enqueue('Python')
c1.enqueue(4)
c1.display()
print()

c1.enqueue('Snarib')
c1.enqueue(7)           # Prints: Circular queue is full
c1.display()
print()

c1.dequeue()
c1.dequeue()
c1.display()            # Prints the remaining items cleanly
