import sys
import time

# https://www.iteramos.com/pregunta/81246/el-tiempo-de-complejidad-del-algoritmo-de-euclides
# The most complexity cases for mcm is calculation of fibonacci numbers
# https://catonmat.net/tools/generate-fibonacci-numbers
# The profiling does with 20 to 40 fibonacci

# O(n) where the max n is x+y (getting with hard mode)
def mcm_cycles(x, y):
	if(x<=0 or y<=0):				# O(1)
		return 0					# O(1)
	factorX=1						# O(1)
	factorY=1						# O(1)
	while True:						# O(x+y) -> number of max iterations, 
									# iter per x factor and y factor to 
									# get an equal multiply factor result
		if(x*factorX==y*factorY):	# O(1) -> factor multiply operation 
									# is equal between numbers
			# returns a mcm
			return x*factorX		# O(1)

		if(x*factorX>y*factorY):	# O(1)
			factorY+=1				# O(1)
		else:						# O(1)
			factorX+=1				# O(1)

# with prim factor
def prim_factor_multiply(n):
	result=1
	while n>1:
		for i in range(2, n+1):
			if(n%i==0):
				result=i*result
				n=int(n/i)
				break
	return result

def mcm_prim_factor(x, y):
	primResultX=prim_factor_multiply(x)
	primResultY=prim_factor_multiply(y)

	if(primResultX>primResultY):
		return primResultX
	else:
		return primResultY


if __name__ == "__main__":
	
	# Instance variable for file control
	fileProfiling=open("mcm cycles profile.csv", "a", encoding="utf-8")

	# Get start time to get lapse time execution
	start = time.time()

	# start to get python memory allocations
	#tracemalloc.start()

	mcm_cycles(int(sys.argv[1]), int(sys.argv[2]))

	# Get end time to get lapsed
	end = time.time()

	# Write in file the result of time and memory profiling
	# fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
	fileProfiling.write("{},{}\n".format(str(sys.argv[1])+"."+str(sys.argv[2]), end-start))
	fileProfiling.close()

	# stop get python memory allocations
	#tracemalloc.stop()
