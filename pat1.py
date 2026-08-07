''' Spiral pattern '''

num = int(input("Enter the number: "))
result = [[0]*num for _ in range(num)]
n = 1    # to display the values
low = 0  # start the range
high = num - 1   # end range
count = int((num+1)/2)   # to get the outer loop count

for i in range(count):
    # inner loop 1
    for j in range(low, high + 1):
        result[i][j] = n
        n += 1

    # inner loop 2
    for j in range(low+1, high+1):
        result[j][high] = n
        n += 1

    # inner loop 3
    for j in range(high-1, low-1, -1):
        result[high][j] = n
        n += 1

    # inner loop 4
    for j in range(high-1, low, -1):
        result[j][low] = n
        n += 1

    low += 1
    high -= 1

print("Result :")
for i in result:
    for j in i:
        print(j, end=" ")
    print()
