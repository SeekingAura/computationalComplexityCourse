import random
import time

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

    if l < left:
        array[k:k+left-l]=leftPart[l:]
        k += left-l
    
    if r < right:
        array[k:k+right-r]=rightPart[r:]

def sort(array, left, right):

    if left >= right: return

    middle = int ((left + right )/ 2)
    
    sort(array, left, middle)
    sort(array, middle + 1, right)

    leftPart = array[left: middle + 1]
    rightPart = array[middle + 1: right + 1]

    merge(array, leftPart, rightPart, left)

if __name__ == "__main__":
    #x = [4,3,2,1,0,-1,-2,-3,-4]
    import sys
    start = time.time()
    x = [random.randint(0,100) for i in range (int(sys.argv[1]))]
    end = time.time()

    print ("initializing time ", end - start)

    start = time.time()
    #print(x, '\n')
    tracemalloc.start()
    sort(x, 0, len(x) - 1)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    end = time.time()
    #print(x)
    print ("ordering time ", end - start)
