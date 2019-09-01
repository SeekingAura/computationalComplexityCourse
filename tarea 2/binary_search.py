# Import python standar libraries
import sys
import os
import random
import time

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

# Search a item secuentially in an ordered array and return the index of vector
# (first time appears) if the item doesn't exist return None
def binary_search(array, l, r, item):
	middle=int(l+(r-l)/2)

	comparisions[0]+=1
	if(array[middle]==item):
		# For measure memory
		result[0]=middle
		return middle

	comparisions[0]+=1
	# Case never found item in array
	if(l>r):
		return None

	comparisions[0]+=1
	if(item>array[middle]):
		return binary_search(array, middle+1, r, item)
	else:
		return binary_search(array, l, middle-1, item)



if __name__=="__main__":
	# Close program if not are 3 arguments (file name, array File or 
	# size for random array and value to search)
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $arrayFileOrSizeNum $valueToSearch\n'.format(sys.argv[0]))
		os._exit(1)

	if(sys.argv[1].isdigit()):
		# Create random array of argv [1] size (n)
		array = [random.randint(0,100) for i in range(int(sys.argv[1]))]+[3]
	else:
		dataInputFile=open(sys.argv[1], "r", encoding="utf-8")
		array=eval(dataInputFile.read())

	# define vars for count comparisions and swap in recursion with reference
	comparisions=[0]
	result=[None]

	# Get start time to get lapse time execution
	start = time.time()

	# start to get python memory allocations
	tracemalloc.start()

	# Create instance of main process
	# process = psutil.Process(os.getpid())

	# Run sort algorithm with random array
	# result=binary_search(array, 0, len(array)-1, int(sys.argv[2]))

	memoryUsed=memory_usage(proc=[binary_search, [array, 0, len(array)-1, int(sys.argv[2])]], max_usage=True, include_children=True)[0]

	# Get end time to get lapse 
	end = time.time()

	# Instance variable for file control
	fileProfiling=open("binary_search profiling.csv", "a", encoding="utf-8")

	# Write in file the result of time and memory profiling (pos 1 is peak in python interpreter)
	# fileProfiling.write("{},{},{},{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start, comparisions[0], sys.argv[2], result))

	# Write in file the result of time and memory profiling
	# wset is Mem Usage in windows, same to rss (Resident Set Size) in linux
	fileProfiling.write("{},{},{},{},{},{},{}\n".format(len(array), memoryUsed, tracemalloc.get_traced_memory()[1], end-start, comparisions[0], sys.argv[2], result[0]))
	fileProfiling.close()

	# stop get python memory allocations
	tracemalloc.stop()