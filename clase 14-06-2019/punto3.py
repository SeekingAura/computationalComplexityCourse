import sys
import random

def randomVector(n):
    result=[]
    iterator=0
    while iterator<n:
        result.append(random.randint(-sys.maxsize, sys.maxsize))
        iterator+=1