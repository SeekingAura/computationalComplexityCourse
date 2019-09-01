# Import standard Python Modules
import sys
import os
import random

if __name__ == "__main__":
	if(len(sys.argv)!=3):
		sys.stderr.write('Usage: "{0}" $maxIterationFactor $Resetcsvs\n'.format(sys.argv[0]))
		os._exit(1)

	nameOutputFile="input python array.txt"

	if(sys.argv[2]=="True"):
		sortCsvFiles=["bubble_sort profiling.csv", "merge_sort profiling.csv", "quick_sort profiling.csv", "countingsort_sort profiling.csv"]
		# sortCsvFiles=["countingsort_sort profiling.csv"]
		for fileName in sortCsvFiles:
			# Re-write file's csv with respective column headers (if 
			# already data in file this is deleted)
			dataCsvFile=open(fileName, "w", encoding="utf-8")

			# Write Column headers in file
			dataCsvFile.write("vector_size,memory_peak_rss,memory_peak_python_interpreter,execute_time,comparisions,swappings\n")
			
			# Close file for update in disk
			dataCsvFile.close()

		searchCsvFiles=["secuential_search profiling.csv", "binary_search profiling.csv"]
		for fileName in searchCsvFiles:
			# Re-write file's csv with respective column headers
			dataCsvFile=open(fileName, "w", encoding="utf-8")

			# Write array in file
			dataCsvFile.write("vector_size,memory_peak_rss,memory_peak_python_interpreter,execute_time,comparisions,value_to_search,result\n")

			# Close file for update in disk
			dataCsvFile.close()

	# array size start in 20, on first time for each iteration increases 
	# 10 until reach 100, the next iterations start in 200 for each iteration
	# increases value in 100 until reach 1000, continue with this way until
	# reach the max array size 10^(maxiterationFactor+1)
	iteratorFactor=1000000
	for iterationFactorTime in range(int(sys.argv[1])):
		# increases iterator factor in 10^iter
		iteratorFactor*=10
		for iterationNumber in range(2, 11):
			# Create vector with iternumber*10^iterationFactorTime+1
			array = [random.randint(0,100) for i in range(iterationNumber*iteratorFactor)]
			
			# Instance file object
			dataOutputFile=open(nameOutputFile, "w", encoding="utf-8")

			# Write array on file
			dataOutputFile.write(str(array))

			# Close file for update in disk
			dataOutputFile.close()

			# Execute bubble sort with last created array in file
			# os.system('python "bubble_sort.py" "{}"'.format(nameOutputFile))

			# Execute bubble sort with last created array in file
			os.system('python "merge_sort.py" "{}"'.format(nameOutputFile))

			# Execute quick sort with last created array in file
			os.system('python "quick_sort.py" "{}"'.format(nameOutputFile))

			# Execute counting sort with last created array in file
			os.system('python "counting_sort.py" "{}"'.format(nameOutputFile))

			# Create a random int for search in secuential and binary search
			itemSearch=random.randint(0,100)
			
			# Execute secuential search
			os.system('python "secuential_search.py" "{}" "{}"'.format(nameOutputFile, itemSearch))

			# Execute binary search
			os.system('python "binary_search.py" "{}" "{}"'.format(nameOutputFile, itemSearch))
