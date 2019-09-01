import sys
import time



#O(n)
def sumatoria(n):
	result=0
	iterator=1
	while iterator<=n:
		result+=iterator
		iterator+=1
	
	return result

# O(1)
def sumatoria_optima(n):
	return n*(n+1)/2

if __name__ == "__main__":
	A=int(sys.argv[1])
	startTime=time.time()
	print(sumatoria(A))
	endTime=time.time()
	fileLog=open("punto2.csv", "a",encoding="utf8")
	fileLog.write("{}, {}\n".format(A,endTime-startTime))
	fileLog.close()