def mergeSort(l1):
    if len(l1) > 1:
        mid = len(l1) // 2
        left_list = l1[:mid]
        right_list = l1[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[i]:
                l1[k] = left_list[i]
                i += 1
            else:
                l1[k] = right_list[j]
                j +=1
            k += 1

        # check if any element is remaining in both list
        while i < len(left_list):
            l1[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            l1[k] = right_list[j]
            j += 1
            k += 1


l1 = [8, 7, 11, 1, 5, 9, 2, 4]
print("L1 before merge sort :", l1)
mergeSort(l1)
print("L1 after merge sort :", l1)
