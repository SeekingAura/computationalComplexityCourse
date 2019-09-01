# Inducción matematica
en ocasiones muchas de las soluciones más optiomas son por medio de técnicas máteticas que en una operación para todos los números permita obtener el valor o en si el comportmaiento de la función
## Prueba 1
hipotesis (2k+1)^2-1 === 0 mod 8

## prueba 2
todo número natural que n!>3^(n-2)

probar que k! > 3^(k-2)
**Hipotesis:** k! > 3^(k-2)
**Demostrar:** (k+1)!>3^(k-2)  
(k+1)!>3^(k-2)  

(k+1)!=k!(k+1)  

k!(k+1)>3^(k-2)(k+1)  

Si k>= 3 entonces k+1 -> es si o si mayor que 3 por lo cual que

k!(k+1)>3^(k-2)*3  
k!(k+1)>3^(k-1)  
k!(k+1)>3^(k+1-1)

## Prueba 3
f(1)=25
f(n+1)=f(n)+4

**Hipotesis:** f(n)=25+(n-1)*4
**Demostrar:** f(n+1)25+n*4

# Inducción fuerte o completa
Se supone que la propiedad es valida para m<=k, en lugar de suponer que la propiedad es únicamente válida para k.

## Fibonacci
fib(n)<2^n

fib(1)=1<2^1
fib(2)=1<2^2
fib(3)=2<2^3

fib(n)=1<2^n
fib(n+1)=1<2^(n+1)

f_(k+1)= f_(k-1) +f_k

<2^(k+1)+2^(k)  
=2^(k-1)+2*2^(k-1)  
=(1+2)


# Taller -- De las diapositivas que va enviar luego...


# complejdiades de taller de clase
## fibonnaci complejidad
2^(n)

Se debe a que por cada ejecución se forman 2 ejecucione spor lo cual su base es 2 y n es la cantidad de veces que se formará

## mcm
su complejidad es o(n) donde su n es el factor multiplicativo del maximo para encontrar el valor ya que busca entre los multiplos del maximo

# Tarea
Crear 4 métodos de ordenamiento en vectores, donde se verifique la cantidad de comparaciones que hizo, el tiempo de ejecución, hacer graficas de tiempo donde se comparen complejidad en memoria

* Realizar un informe en formato articulo
* Realizar la implementación
* burbuja y otros 3 más
* De cada método indicar por que y para que es bueno
* Determinar el tiempo
