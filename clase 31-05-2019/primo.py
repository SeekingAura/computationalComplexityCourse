import time
import sys
"""
Evaluate num if is prim
"""
def primoSecuencial(A):
	div=int(A/2)       # divisor value for each iteration
	if(div<2):
		return True
	while div>=2:
		if((A%div)==0):# only happens if divide in a number diferent of value A
			return False
		div-=1
	return True


if __name__ == "__main__":
	# sys.maxsize Max int value python 9223372036854775807
	A=int(input("Ingrese valor entero positivo A a calcular primo\n"))
	startTime=time.time()
	print(primoSecuencial(A))
	endTime=time.time()
	
	print("Tiempo de ejecución {}".format(endTime-startTime))
	print("Profiling {}".format(sys.getsizeof(primoSecuencial(A))))
