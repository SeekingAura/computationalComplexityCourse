import sys

def factorial(n):
    result=1
    for i in range(2,n):
        result=result*i

    return result


def combinatoria(n, k):
    if(n<=0 or k<0 or k>n):# error case
        return 0

    return factorial(n)/(factorial(k)*factorial(n-k))

if __name__ == "__main__":
    print(combinatoria(10, 10))
    