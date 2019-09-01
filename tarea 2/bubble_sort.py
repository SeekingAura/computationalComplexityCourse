# https://sci-hub.tw/https://dl.acm.org/citation.cfm?id=611918
# https://www.geeksforgeeks.org/bubble-sort/
import random
import time
import sys
import os

# https://realpython.com/python-memory-management/

# https://stackoverflow.com/questions/22732932/how-to-get-the-max-memory-usage-of-a-program-using-psutil-in-python
# https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info
# import psutil

# memory not allocated by the python interpreter is not seen by tracemalloc
# external memory (pyc) depend of operative system
# https://docs.python.org/3/library/tracemalloc.html
import tracemalloc

# https://pypi.org/project/memory-profiler/
from memory_profiler import memory_usage

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
				swappings[0]+=1
			comparisions[0]+=1
			
if __name__ == "__main__":
	# Close program if not are 3 arguments (file name, array File)
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $arrayFileOrSizeNum\n'.format(sys.argv[0]))
		os._exit(1)
		
	# Create random array of argv [1] size (n)
	if(sys.argv[1].isdigit()):
		array = [random.randint(0,100) for i in range(int(sys.argv[1]))]
	else:
		dataInputFile=open(sys.argv[1], "r", encoding="utf-8")
		array=eval(dataInputFile.read())
		dataInputFile.close()
		
	# define vars for count comparisions and swap in recursion with reference
	comparisions=[0]
	swappings=[0]

	# Get start time to get lapse time execution
	start = time.time()

	# process = psutil.Process(os.getpid())
	# start to get python memory allocations
	tracemalloc.start()

	# Run sort algorithm with random array
	# bubble_sort(array)

	memoryUsed=memory_usage(proc=[bubble_sort, [array]], max_usage=True, include_children=True)[0]

	# Get end time to get lapse 
	end = time.time()
	
	# Instance variable for file control
	fileProfiling=open("bubble_sort profiling.csv", "a", encoding="utf-8")

	# Write in file the result of time and memory profiling (pos 1 is peak in python interpreter)
	# fileProfiling.write("{},{},{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))

	# Write in file the result of time and memory profiling
	# wset is Mem Usage in windows, same to rss (Resident Set Size) in linux
	fileProfiling.write("{},{},{},{},{},{}\n".format(len(array), memoryUsed, tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))
	fileProfiling.close()

	# stop get python memory allocations
	tracemalloc.stop()