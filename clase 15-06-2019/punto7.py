import sys

# O(n) where n is max result of mcm bettwheen numbers
def mcm_cicles(x, y):
    if(x<=0 or y<=0):
        return 0
    if(x<y):#swaping
        x,y=y,x
    # factor control for multiply
    factorX=1
    factorY=1

    while True:
        if(x*factorX==y*factorY):
            # returns a mcm
            return x*factorX

        if(x*factorX>y*factorY):
            factorY+=1
        else:
            factorX+=1

# with prim factor
def prim_factor_multiply(n):
    result=1
    while n>1:
        for i in range(2, n+1):
            if(n%i==0):
                result=i*result
                n=int(n/i)
                break
    return result

def mcm_prim_factor(x, y):
    primResultX=prim_factor_multiply(x)
    primResultY=prim_factor_multiply(y)

    if(primResultX>primResultY):
        return primResultX
    else:
        return primResultY


if __name__ == "__main__":
    
    print(mcm_cicles(4, 36))

