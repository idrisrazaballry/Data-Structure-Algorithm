## Dynamic Programming

'''
- It is technique by solving bigger problem by breaking down into sub - problems

# Steps:
- Break the bigger problem into smaller parts 
- Store the value of each sub problem into the specific location
- Reuse the value when it is neccessary
'''

# 1. WAP to display nth fibonacci number

def nth_fib_num(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    
    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(nth_fib_num(int(input("Enter the number :"))))