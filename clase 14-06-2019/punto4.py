import sys
import random

def matrix_random(n, m):
    result=[]
    for i in range(n):
        result.append([])
        for j in range(m):
            result[-1].append(random.randint(-sys.maxsize, sys.maxsize))
    return result
