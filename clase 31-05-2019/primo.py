import time
import sys
"""
Evaluate num if is prim
"""

def primeFermat(A):
	return (2**(A-1)%A)==1

# https://en.wikipedia.org/wiki/Primality_test
def primeSecuentialOptimal(A):
	if(A<=3):
		return True
	if(A%3==0 or A%2==0):
		return False
	div=5
	while div**div <=A:
		if A%div==0 or A%(div+2)==0:
			return False
		div+=6
	
	return True

def primeSecuential(A):
	
	if(A<=3):
		return True
	div=int(A/2)       # divisor value for each iteration
	while div>=2:
		if((A%div)==0):# only happens if divide in a number diferent of value A
			return False
		div-=1
	return True


if __name__ == "__main__":
	# sys.maxsize Max int value python 9223372036854775807
	# https://www.bigprimes.net/archive/prime/
	# 3241619007
	# 6507*2**1409602+1
	# python -m profile primo.py
	A=int(sys.argv[1])
	startTime=time.time()
	print(primeSecuentialOptimal(A))
	endTime=time.time()
	fileLog=open("timeStamp.txt", "a",encoding="utf8")
	fileLog.write("{}	{}	{}\n".format(A,endTime-startTime,sys.getsizeof(primeSecuentialOptimal(A))))
	fileLog.close()

	#fileLog=open("timeStampFermat.txt", "a",encoding="utf8")
	#startTime=time.time()
	#print(primeFermat(A))
	#endTime=time.time()
	#fileLog.write("{}	{}	{}\n".format(A,endTime-startTime,sys.getsizeof(primeFermat(A))))
	#fileLog.close()
	
