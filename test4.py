'''WAP to solve the given expression into postfix evaluation'''

def postfix_eval(expression):
    stack = []

    for char in expression:
        if ord(char) >= 49 and ord(char) <=57:
            stack.append(int(char))
        else:
            n2 = stack.pop()
            n1 = stack.pop()

            if char == "+":
                stack.append((n1+n2))
            elif char == "-":
                stack.append((n1-n2))
            elif char == "*":
                stack.append((n1*n2))
            elif char == "/":
                stack.append((n1/n2))
            elif char == "^":
                stack.append((n1**n2))
    return stack.pop()

exp='231*+'

print("Postfix evaluation of :", exp)
print(postfix_eval(exp))
