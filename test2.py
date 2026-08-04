# WAP to reverse the given string using stack implementation

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

s = stack()
str = input("Enter the string: ")
print("Given string --> ", str)
for i in range(len(str)):
    s.push(str[i])

print()

res = ""
while (len(s.s1)) != 0:
    res += s.pop()
print("Reversed string --> ",res)
