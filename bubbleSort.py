def bubble_sort(l1):
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            # if l1[i] < l1[j]: # this is for descending order
            if l1[i] > l1[j]: # this is for ascending order
                l1[i], l1[j] = l1[j], l1[i]

l1= [4,7,2,8,5,3]
print("Before sorting :", l1)
bubble_sort(l1)
print("After sorting :", l1)