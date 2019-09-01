import sys

# es n^3
def matrix_mul(matrixA, matrixB):
	result=[]
	for row in matrixA:
		result.append([])
		for col in matrixB:
			tempResult=0
			for rowI, colI in zip(row, col)
				tempResult+=rowI*colI
			result[-1].append(tempResult)

		
	return result

	
#1 2 3
#4 5 6
#7 8 9