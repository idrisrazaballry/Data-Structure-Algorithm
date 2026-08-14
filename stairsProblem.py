# WAP to find the total number of ways to climb stairs

n = int(input("Enter the number of stairs: "))

if n == 0 or n == 1:
    print(1)
else:
    first = 1
    second = 1

    for i in range(2, n + 1):
        total = first + second
        first = second
        second = total

    print(second)
