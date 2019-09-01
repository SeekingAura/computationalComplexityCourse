import sys


# 2^(n) -> 
def fibonnacciRecursivo(n):
	if(n==1 or n==2):
		return 1
	return fibonnacciRecursivo(n-1)+fibonnacciRecursivo(n-2)


# O(n)
def fibonacciOptimal(n):
	if(n==1 or n==2):
		return 1
	result=1
	last=1
	for i in range(n-2):
		result+=last
		last=result-last
	return result
		
		

if __name__ == "__main__":
	print(fibonacciOptimal(int(input("ingrese n\n"))))