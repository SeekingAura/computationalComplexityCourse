import sys

# es n^3
def matrix_mul(matrixA, matrixB):
	result=[]
	for row in matrixA:
		result.append([])
		for col in matrixB:
			result[-1].append(row*col)
		
	return result

	