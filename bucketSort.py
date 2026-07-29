# It is used for huge amount of data

from math import sqrt, ceil

def bubbleSort(l1):
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            # if l1[i] < l1[j]: # this is for descending order
            if l1[i] > l1[j]: # this is for ascending order
                l1[i], l1[j] = l1[j], l1[i]
    return l1

def bucketSort(l1):
    # find the number of buckets to create
    total_buckets = round(sqrt(len(l1)))

    # create a total buckets using nested list
    buckets = []
    for i in range(total_buckets):
        buckets.append([])
    print(buckets)

    # insert each to its respective bucket
    for val in l1:
        idx = ceil((val * total_buckets) / max(l1))
        buckets[idx - 1].append(val)
    print(buckets)

    # sort each buckets
    for i in range(len(buckets)):
        buckets[i] = bubbleSort(buckets[i])
    print(buckets)

    # merge all the buckets
    k = 0
    for i in range(total_buckets):
        for j in range(len(buckets[i])):
            l1[k] = buckets[i][j]
            k += 1

    print(l1)

l1 = [8,3,9,5,3,8,6]
bucketSort(l1)