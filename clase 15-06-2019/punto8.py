import sys
import resource
import os
#import resource, sys



def factorial(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def combinatoria(n, k):
    if(n<=0 or k<0 or k>n):# error case
        return 0
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def factorial_recursive(n):
    if(n==1):
        return 1
    return factorial_recursive(n-1)*n

def combinatoria_recursive(n, k):
    if(n<=0 or k<0 or k>n):# error case
        return 0
    return int(factorial_recursive(n)/(factorial_recursive(k)*factorial_recursive(n-k)))


if __name__ == "__main__":
    #print(combinatoria(20, 18))
    # only linux
    resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
    #sys.setrecursionlimit(10**6)
    print(combinatoria_recursive(4000, 860))
    