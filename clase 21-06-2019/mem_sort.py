# Standar libraries of python
import sys
import random
import os
import time

# https://pypi.org/project/memory-profiler/

if __name__=="__main__":
	if(len(sys.argv)!=1):
		sys.stderr.write('Usage: "{0}" $hostAddress\n'.format(sys.argv[0]))
		os._exit(1)
	# sys.getsizeof()
	# (2**30)-1 -> max value that usage 28 bytes pet integer value
	vectorX=[random.randint(-((2**30)-1), (2**30)-1) for i in range(10)]