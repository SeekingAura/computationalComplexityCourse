Complejidad de binaria 
```
T(n)=1+t(n/2)  
    =1+1+t(n/4)
    =1+1+1+t(n/8)
```

Los 1+1+1+1 es un valor k, y por el otro lado la sucesión determina el valor de su base por lo cual complejidad es O(log_2(n))


