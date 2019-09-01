import random
import time
import sys

# https://docs.python.org/3/library/tracemalloc.html
import tracemalloc

"""
ordering
"""
def countingSort(array):
    _min = min(array)
    _max = max(array)
    bot = _min * -1

    if _min < 0:
        size = bot + (_max + 1)
    else:
        size = _max + 1
        bot = 0
    
    # get times are a value, where the index is the value and the value is the times are in vector
    count = [0] * size
    for item in array:
        index = bot + item
        count[index] += 1
    
    # get number "distance" to get a value in the list from the value with index
    for i in range(1, size):
        count[i] += count[i-1] 

    result = [0] * len(array)
    for item in array:
        index = bot + item
        result[count[index] - 1] = item
        count[index] -= 1
    
    return result

if __name__ == "__main__":
    # Create random array of argv [1] size (n+2) where 2 is -100 max value and 100 min value
    array = [random.randint(-100,100) for i in range(int(sys.argv[1]))]+[-100, 100]
    
    # Instance variable for file control
    fileProfiling=open("countingsort sort profile.csv", "a", encoding="utf-8")

    # Get start time to get lapse time execution
    start = time.time()
    
    # start to get python memory allocations
    tracemalloc.start()
    
    # Run sort algorithm with random array
    array = countingSort(array)

    # Get end time to get lapsed
    end = time.time()

    # Write in file the result of time and memory profiling
    fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
    fileProfiling.close()

    # stop get python memory allocations
    tracemalloc.stop()