def partition(l1, start, end):
    pivot = l1[end]
    i = start
    j = end - 1

    while i <= j:
        while i <= j and l1[i] < pivot:
            i += 1

        while i <= j and l1[j] >= pivot:
            j -= 1

        if i < j:
            l1[i], l1[j] = l1[j], l1[i]
            i += 1

    l1[i], l1[end] = l1[end], l1[i]
    return i


def quickSort(l1, start, end):
    
    if start < end :
        pi = partition(l1, start, end)
        quickSort(l1, start, pi - 1)
        quickSort(l1, pi + 1, end)


l1 = [5, 8, 3, 2, 7, 9, 8]
print("Before sorting :", l1)
quickSort(l1, 0, len(l1) - 1)
print("After sorting :", l1)

'''
Overall Logic
*  Choose the last element as the pivot.
*  Move all elements smaller than the pivot to the left.
*  Move all elements greater than or equal to the pivot to the right.
*  Place the pivot in its correct sorted position.
*  Repeat the same process on the left and right subarrays recursively.
*  Stop when a subarray has 0 or 1 element, because it is already sorted.


'''