 # 0, 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 
import time
import sys
"""
get fibonacci series at n iterations
"""

def fibonnacciRecursivo(n):
	if(n==1):
		return 0
	if(n==2):
		return 1
	return fibonnacciRecursivo(n-1)+fibonnacciRecursivo(n-2)

if __name__ == "__main__":
	# sys.maxsize Max int value python 9223372036854775807
	A=int(input("Ingrese valor entero positivo A a calcular fibonacci\n"))
	startTime=time.time()
	print(fibonnacciRecursivo(A))
	endTime=time.time()
	
	print("Tiempo de ejecución {}".format(endTime-startTime))
	print("Profiling {}".format(sys.getsizeof(fibonnacciRecursivo(A))))