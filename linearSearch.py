''' Insertion Sort  ''' 

# It is also known as sequential search which help us to search for the given element is present or not in the given list 
# In this iterate through each element and compare with given element, if it is True print its index and break the loop
# If all the iteration is completed while coming out of the for loop print value not found in the else block

def linearSearch(num, l1):
    for i in range(len(l1)):
        if l1[i] == num:
            print(f'{num} is found at {i}')
            break
    else:
        print(f'{num} is not found')


l1 = [2,7,4,3,6,0,4,7]
num = int(input("Enter the number :"))
linearSearch(num, l1)