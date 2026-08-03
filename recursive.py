# Rules to follow recursion
'''
1. Need to have different input in each fucntion call
2. Need to pass higher or lower input to make problem smaller
3. Base Condition. 

'''

# 1. def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# def sumOfNums(n):
#     if n==1:
#         return 1
#     else:
#         return n+sumOfNums(n-1)
# print(sumOfNums(10))


# def sumofdigit(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sumofdigit(n//10)


# print(sumofdigit(81265))
# print(sumofdigit(83455))
# print(sumofdigit(85485))


''' WAP to convert decimal to binary using recursion '''

# def decToBin(n):
#     if n==0:
#         return 0
#     else:
#         return n%2+10*decToBin(n//2)



# print(decToBin(10))
# print(decToBin(15))
# print(decToBin(8))


# def dtb(n):
#     if n>1:
#         dtb(n//2)
#     print(n%2, end='') 

# dtb(10)
# print()
# dtb(20)
# print()
# dtb(30)
# print()


''' WAP to display only even numbers upto 10 using recursion '''
# def displayEven(n):
#     if n<=10:
#         if n%2==0:
#             print(n, end=' ')
#         displayEven(n+1)

# displayEven(1)
# print()


''' WAP to display only odd numbers upto 10 using recursion '''
# def displayOdd(n):
#     if n<=10:
#         if n%2!=0:
#             print(n, end=' ')
#         displayOdd(n+1)
# displayOdd(1)
# print()


''' SUm of given elements in list using recursion '''
# def sumOfElements(lst):
#     if not lst:
# #   if len(lst)==0:
#         return 0
#     else:
#         return lst[0] + sumOfElements(lst[1:])

# # my_list = [1, 2, 3, 4, 5]
# my_list = (2,3,7,5)
# print("Sum of elements in the list:", sumOfElements(my_list))

''' WAP to display the string in reverse manner '''

def rever(str):
    if len(str)==0:
        return ""
    else:
        return str[-1]+rever(str[:-1])
    
s1='python'
print(rever(s1))
print()
s2='sirdi'
print(rever(s2))


''' WAP to convert the first and last char of a word in list into upper case using recursion method'''

lst=['python', 'coding', 'is', 'awesome', 'when','we','practice']