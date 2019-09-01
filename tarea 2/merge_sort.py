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

# k is actual evaluate part of array
def merge(array, leftPart, rightPart, k):
	l = 0; r = 0
	left = len(leftPart); right = len(rightPart)

	while l < left and r < right:
		comparisions[0]+=1
		if leftPart[l] < rightPart[r]:
			array[k] = leftPart[l]
			l += 1
			swappings[0]+=1
		else:
			array[k] = rightPart[r]
			r += 1
			swappings[0]+=1
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

	# array slice in python is [from:to]
	# where from is exactly index and to 
	# is n-1 where n is to value

	# Takes in array from left to middle
	leftPart = array[left: middle + 1]

	# Takes in array from middle+1 to right
	rightPart = array[middle + 1: right + 1]

	merge(array, leftPart, rightPart, left)

if __name__ == "__main__":
	# Close program if not are 3 arguments (file name, array File)
	if(len(sys.argv)!=2):
		sys.stderr.write('Usage: "{0}" $arrayFileOrSizeNum\n'.format(sys.argv[0]))
		os._exit(1)
	
	if(sys.argv[1].isdigit()):
		# Create random array of argv [1] size (n)
		array = [random.randint(0,100) for i in range (int(sys.argv[1]))]
	else:
		dataInputFile=open(sys.argv[1], "r", encoding="utf-8")
		array=eval(dataInputFile.read())
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
	# sort(array, 0, len(array) - 1)

	memoryUsed=memory_usage(proc=[sort, [array, 0, len(array) - 1]], max_usage=True, include_children=True)[0]

	# Get end time to get lapsed
	end = time.time()
	
	# Instance variable for file control
	fileProfiling=open("merge_sort profiling.csv", "a", encoding="utf-8")

	# Write in file the result of time and memory profiling (pos 1 is peak in python interpreter)
	# fileProfiling.write("{},{},{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))

	# Write in file the result of time and memory profiling
	# wset is Mem Usage in windows, same to rss (Resident Set Size) in linux
	fileProfiling.write("{},{},{},{},{},{}\n".format(len(array), memoryUsed, tracemalloc.get_traced_memory()[1], end-start, comparisions[0], swappings[0]))
	fileProfiling.close()

	# stop get python memory allocations
	tracemalloc.stop()