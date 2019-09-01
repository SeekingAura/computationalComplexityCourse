# https://sci-hub.tw/https://dl.acm.org/citation.cfm?id=611918
# https://www.geeksforgeeks.org/bubble-sort/
import random
import time
import sys

# https://docs.python.org/3/library/tracemalloc.html
import tracemalloc


"""
swapping the adjacent elements if they are in wrong order.
"""
# min to max values
def bubble_sort(vector):
    n=len(vector)
    for i in range(n):
        # Check actual value with next value
        for j in range(0, n-i-1):
            if(vector[j]>vector[j+1]):
                # Swapping
                vector[j], vector[j+1]=vector[j+1], vector[j]
            
if __name__ == "__main__":
    # Create random array of argv [1] size (n)
    array = [random.randint(0,100) for i in range(int(sys.argv[1]))]

    # Instance variable for file control
    fileProfiling=open("bubblesort profiling.csv", "a", encoding="utf-8")
    
    # Get start time to get lapse time execution
    start = time.time()

    # start to get python memory allocations
    tracemalloc.start()

    # Run sort algorithm with random array
    bubble_sort(array)

    # Get end time to get lapse 
    end = time.time()
    
    # Write in file the result of lapsed time and current measure memory
    fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
    fileProfiling.close()

    # stop get python memory allocations
    tracemalloc.stop()