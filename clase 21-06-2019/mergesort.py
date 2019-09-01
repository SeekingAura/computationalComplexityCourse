import random
import time
import sys

# https://docs.python.org/3/library/tracemalloc.html
import tracemalloc

def merge(array, leftPart, rightPart, k):
    l = 0; r = 0
    left = len(leftPart); right = len(rightPart)

    while l < left and r < right:
        if leftPart[l] < rightPart[r]:
            array[k] = leftPart[l]
            l += 1
        else:
            array[k] = rightPart[r]
            r += 1
        k += 1

    while l < left:
        array[k] = leftPart[l]
        l += 1; k += 1
    
    while r < right:
        array[k] = rightPart[r]
        r += 1; k += 1

def sort(array, left, right):

    if left >= right: return

    middle = int ((left + right )/ 2)
    
    sort(array, left, middle)
    sort(array, middle + 1, right)

    leftPart = array[left: middle + 1]
    rightPart = array[middle + 1: right + 1]

    merge(array, leftPart, rightPart, left)

if __name__ == "__main__":
    # Create random array of argv [1] size (n)
    array = [random.randint(0,100) for i in range (sys.argv[1])]

    # Instance variable for file control
    fileProfiling=open("countingsort sort profile.csv", "a", encoding="utf-8")

    # Get start time to get lapse time execution
    start = time.time()

    # start to get python memory allocations
    tracemalloc.start()

    # Run sort algorithm with random array
    sort(array, 0, len(x) - 1)

    # Get end time to get lapsed
    end = time.time()

    # Write in file the result of time and memory profiling
    fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
    fileProfiling.close()

    # stop get python memory allocations
    tracemalloc.stop()