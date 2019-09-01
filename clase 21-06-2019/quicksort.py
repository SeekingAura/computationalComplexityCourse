import random
import time
import sys

# https://docs.python.org/3/library/tracemalloc.html
import tracemalloc

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def quickSort(array, left, right):
    
    if left >= right: return
    
    pivot = int((left + right) / 2)

    l = left
    r = right

    while True:
        while array[l] < array[pivot]: l += 1
        while array[r] > array[pivot]: r -= 1

        if l == r: break
        
        swap(array, l, r)

        if l == pivot:
            pivot = r
            l += 1
        elif r == pivot:
            pivot = l
            r -= 1
        else:
            l += 1
            r -= 1


    quickSort(array, left, pivot-1)
    quickSort(array, pivot + 1, right)

if __name__ == "__main__":
    # Create random array of argv [1] size (n)
    array = [random.randint(0,100) for i in range(sys.argv[1])]

    # Instance variable for file control
    fileProfiling=open("quicksort profiling.csv", "a", encoding="utf-8")

    # Get start time to get lapse time execution
    start = time.time()

    # start to get python memory allocations
    tracemalloc.start()

    # Run sort algorithm with random array
    quickSort(array, 0, len(array) - 1)

    # Get end time to get lapsed
    end = time.time()

    # Write in file the result of time and memory profiling
    fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
    fileProfiling.close()

    # stop get python memory allocations
    tracemalloc.stop()