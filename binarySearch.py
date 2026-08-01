def binarySearch(num, l1):
    start = 0
    end = len(l1) - 1

    while start < end:
        mid = (start + end) // 2
        if l1[mid] == num:
            return mid
        elif num < l1[mid]:
            end = mid -1
        elif num > l1[mid]:
            start = mid + 1
        else:
            return (f'{num} is found')
        break
    else:
        return (f'{num} is not found')

l1 = [3,5,7,8,9]
print(binarySearch(9, l1))