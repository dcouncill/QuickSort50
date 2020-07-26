import numpy as np
arr = np.random.randint(low=1, high=10000, size=50)
print(arr)

import random
def quickSort(arr,start,stop):
    if(start < stop):
         pivotindex = partitionrand(arr, start, stop)
         quickSort(arr, start, pivotindex -1)
         quickSort(arr,pivotindex + 1, stop)

    def partitionrand(arr,start,stop):
        randpivot = random.randrange(start, stop)
        arr[start], arr[randpivot] = arr[randpivot], arr[start]
        return partition(arr, start, stop)

    def partition(arr,start,stop):
        pivot = start
        i = start + 1
        for j in range(start + 1, stop +1):
            if arr[j] <= arr[pivot]:
                 arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
        arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
        pivot = i - 1
        return(pivot)
        quickSort(arr, 0, len(arr)-1)
print(arr)

import timeit
code_to_test = """ 
import numpy as np
arr = np.random.randint(low=1, high=10000, size=50)
print(arr)

import random
def quickSort(arr,start,stop):
    if(start < stop):
         pivotindex = partitionrand(arr, start, stop)
         quickSort(arr, start, pivotindex -1)
         quickSort(arr,pivotindex + 1, stop)

    def partitionrand(arr,start,stop):
        randpivot = random.randrange(start, stop)
        arr[start], arr[randpivot] = arr[randpivot], arr[start]
        return partition(arr, start, stop)

    def partition(arr,start,stop):
        pivot = start
        i = start + 1
        for j in range(start + 1, stop +1):
            if arr[j] <= arr[pivot]:
                 arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
        arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
        pivot = i - 1
        return(pivot)
        quickSort(arr, 0, len(arr)-1)
print(arr) """
elapsed_time = timeit.timeit(code_to_test, number=100)
print(elapsed_time)
