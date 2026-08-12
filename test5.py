# WAP to check the given parenthesis is balanced or not

def is_balanced(s1):
    stack = []
    paranthesis = {'}':'{', ']':'[', ')':'('}

    for char in s1:
        if char in paranthesis.values():
            stack.append(char)
        elif char in paranthesis:
            if not stack or stack[-1] != paranthesis[char]:
                return False
            stack.pop()

    return len(stack) == 0


# s1 = '([{}])'
s1 = '({}])'
if is_balanced(s1):
    print("Balanced")
else:
    print("Not balanced")