#Binary Search & Quick sort Algorithm

import random
import timeit

#Generate array of 1000 random numbers

nums = []
x = 0
size = int(input("Please enter size of Array to Sort (int): \n"))

while x < size:
    x += 1
    nums.append(random.randint(0, size))

message = "\n" + "Unsorted Array of size {}: \n"
print(message.format(size))
print(nums)


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = array[high], array[i +1]
    
    return i +1


def quicksort(array, low, high):
  if low < high:
      
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quicksort(array, low, pi - 1)

    # recursive call on the right of pivot
    quicksort(array, pi + 1, high)


size = len(nums)

#Calculate how long program takes to run
start = timeit.default_timer()
quicksort(nums, 0, size - 1)
stop = timeit.default_timer()

txt = "\n Array Sorted Using QuickSort in {} milliseconds \n"

print(txt.format((stop-start)*1000))

print(nums)

def binarysearch(array, low, high, target):

    if high >= low:
        middle = (high + low) // 2

        if array[middle] == target:
            return middle
    
        elif array[middle] > target:
        
            return binarysearch(array, low, middle-1, target)
            
        elif array[middle] < target:
        
            return binarysearch(array, middle +1, high, target)
  
    else:
        return -1

target = int(input("\n" + "Please Input a Target Number: "))

start = timeit.default_timer()
result = binarysearch(nums, 0, len(nums)-1, target)
stop = timeit.default_timer()

if (result != -1):
    string = "\n" + "Binary Search Found Target Number At Index {} in {} milliseconds"
    print(string.format(result, (stop - start) *1000))
else:
    print("\n" + "Target Number is not in Array")
