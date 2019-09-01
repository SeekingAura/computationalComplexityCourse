1. Calcular la complejidad de la asignación:  
```c++
var = 5
```
    La complejida des O(T_k), Tk par ala asignación es 1, por lo tanto por teorema 1 la complejidad es  
**R/=** O(1)

2. Calcular la complejidad de:  
```c++
a = 1;  
b = 2;  
c = 3;
```

**R/=** La complejidad de cada instrucción de asignación es O(1), la complejidad de este caso como todas y cada una no generan ciclos entonces la complejidad seria O(1)+O(1)+O(1) y por teorema 2 la complejidad será el maximo de las complejidades y es **O(1)**

3. Calcular complejidad de:  
float abs (float n)  
```c++
    { if (n < 0)  
	      return –n;
	  else
	      return n;
	}
```

**R/=** La complejidad de una comparación es O(1), la complejidad de este caso es una comparación entonces por lo tanto por teorema 1 la complejidad es 1 **O(1)**

4. Calcular la complejidad de
```c++
int factorial (int n){
    int i, acum;
    i = 0;
    acum = 1;
    while (i < n)
        {  i++;
            acum *= i;
            }
        return acum;
}
```
**R/=** 
* la instanciación de una variable es complejidad 1, la asignación de una variable tambien es complejidad 1, por lo cual la primera linea es complejidad O(2) ya que es la creación de 2 variables, pero por teorema 1 la constante de una complejidad siempre es 1 
* Un ciclo su complejidad es la cantidad de iteraciones que sea el ciclo, en este caso este ciclo va de 0 hasta n-1, es decir se ejecutará n veces, por lo cual su complejidad es O(n)
* El retorno de una función es O(1)

La complejidad total es la suma de las complejidades es decir O(2)+O(n)+O(1), por teorema 2 la complejidad de la función es la complejidad máxima siendo finalente -> O(n)

5. 
```c++
for (i=0; i<5; i++)
	      a[i]=i; 
```

**R/=** En este for se logra una cantidad de iteraciones definida que es 5, lo cual es lo mismo que;

```c++
a[0]=0; 
a[1]=1; 
a[2]=2; 
a[3]=3; 
a[4]=4; 
```

La complejidad de lo anterior es O(5), si aplicamos teorema 1 la complejidad de la sentencia principal es O(1)


6. 

```c++
void inic(int a[], int tam){
    int i;	 
    for (i=0; i<tam; i++)
        a[i]=i;
}
```

**R/=** En la función inic recibe dos parametros un vector de enteros *a* y un entero *tam* instancia un valor entero i lo cual su coomplejidad es O(1), el for hace iteraciones de tanto tam sea, por lo cual la complejidad es O(tam), por teorema 2 la complejidad de la función es el maximo de sus complejidades el cual es O(n) -> lineal




# Taller

1. Hacer una función que reciba un número entero positivo y retorne verdadero si es primo o falso sino. 
2. Hacer una función que reciba un valor N y retorne la sumatoria de los enteros hasta N.
3. Hacer una función que llene un vector (de tamaño N) con números enteros aleatorios (puede ser de 4 cifras).
4. Hacer una función que llene una matriz de tamaño NxM con números aleatorios.
5. Hacer una función que reciba 2 matrices de tamaño NxM y MxP respectivamente y devuelva otra matriz con la multiplicación de las dos primeras

6. Hacer una función que calcule el n-ésimo número de la  serie de fibonacci,
7. Hacer una  función que retorne el mcm (mínimo común múltiplo ) de 2 numeros naturales mayores que  0.
8. Hacer una  función que  calcule  el número de combinaciones , en una expresión de combinación binomial . Conocemos el valor de k y n (n> 0, k>=0 y k<=n). Corresponde a las posibles combinaciones  para seleccionar k elementos de un conjunto de n elementos. Esta expresión está  dada por la fórmula siguiente:  
(n complete k) (n!)/(k!(n-k)!)