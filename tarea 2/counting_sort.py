import random
import time
import sys
import os

# https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference
# https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
import numpy as np

# https://realpython.com/python-memory-management/

# https://stackoverflow.com/questions/22732932/how-to-get-the-max-memory-usage-of-a-program-using-psutil-in-python
# https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info
# import psutil

# https://pypi.org/project/memory-profiler/
from memory_profiler import memory_usage

# memory not allocated by the python interpreter is not seen by tracemalloc
# external memory (pyc) depend of operative system
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
	
	# get times are a value, where the index is the value and the value 
	# is the times are in vector
	count = [0] * size
	for item in array:
		index = bot + item
		count[index] += 1
		comparisions[0]+=1
	
	# get number "distance" to get a value in the list from the value with index
	# for i in np.arange(1, size):
	for i in range(1, size):
		count[i] += count[i-1] 
		comparisions[0]+=1

	# set on list result from distance with vector count
	result = [0] * len(array)
	for item in array:
		index = bot + item
		result[count[index] - 1] = item
		count[index] -= 1

		swappings[0]+=1
	
	del array
	array=result

if __name__ == "__main__":
	# Close program if not are 3 arguments (file name, array File)
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $arrayFileOrSizeNum\n'.format(sys.argv[0]))
		os._exit(1)


	if(sys.argv[1].isdigit()):
		# Create random array of argv [1] size (n)
		# array = np.array([random.randint(0,100) for i in np.arange(int(sys.argv[1]))])
		array = [random.randint(0,100) for i in range(int(sys.argv[1]))]
	else:
		# Open file with array content
		dataInputFile=open(sys.argv[1], "r", encoding="utf-8")

		# read file and parsing to eval python code for use in execution
		# array=eval("np.array("+dataInputFile.read()+")")
		array=eval(dataInputFile.read())

		# Close file for free memory
		dataInputFile.close()
	
	# define vars for count comparisions and swap in recursion with reference
	comparisions=[0]
	swappings=[0]

	# Get start time to get lapse time execution
	start = time.time()
	
	# Create instance of main process
	# process = psutil.Process(os.getpid())
	# start to get python memory allocations
	tracemalloc.start()
	
	# Run sort algorithm with random array
	# countingSort(array)
	memoryUsed=memory_usage(proc=[countingSort, [array]], max_usage=True, include_children=True)[0]

	# Get end time to get lapsed
	end = time.time()

	# Instance variable for file control
	fileProfiling=open("countingsort_sort profiling.csv", "a", encoding="utf-8")

	# Write in file the result of time and memory profiling (pos 1 is peak in python interpreter)
	# fileProfiling.write("{},{},{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))

	# Write in file the result of time and memory profiling
	# wset is Mem Usage in windows, same to rss (Resident Set Size) in linux
	fileProfiling.write("{},{},{},{},{},{}\n".format(len(array), memoryUsed, tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))
	

	# Close file for update in disk
	fileProfiling.close()

	# Stop get python memory allocations
	tracemalloc.stop()

	if(not sys.argv[1].isdigit()):
		# Write file input array with ordered array (for execute secuential 
		# and binary search), if alredy data inf ifle this is deleted
		dataInputFile=open(sys.argv[1], "w", encoding="utf-8")

		# Write array in file
		dataInputFile.write(str(array))
		
		# Close file for update in disk
		dataInputFile.close()

	