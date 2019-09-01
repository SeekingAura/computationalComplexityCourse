# Complejidad y computabilidad
* Estudia el orden de complejidad de un algoritmo que resuelve un problema decidible
* En este se considera 2 tipos de recursos que se requieren durante el proceso de computo
    * Tiempo
    * Memoria
* La complejidad de un algoritmo se expresa como función del tamaño de la entrada del problema, n.
* Se refiere al ratio de crecimiento de los recursos con respecto a n:
    * Ratio de tiempo de ejecución T(n)
    * Ratio del espacio de almacenamiento necesario espacial.

## Concepto
es tratar de encontrar una función f(n) facil de calcular que acote el crecimiento de la función de tiempo > "T_A(n) crece aproximadaemnte como f"

### Clasificación de problemas de decisión
Se hace a base de datos criterios
* Teoria de la computabilidad

De a cuerdo a la teróa de la computabilidad un problema de decisión podrá ser
* Decidible:
    * Si existe un procedimiento mecánico (MT) que lo resuelva
    * Ademas, el procedimiento mecanico debe detenerse para cualquier entrada
* Parcialmente decidible:

Los problemas podrán ser Clase L, NL, P, P-Completo, NP, NP-Completo, NP-Duro
Para esta distincón es necesario considerar el modelo teórico de las máquinas de turing (maquina de estados)
* MT determinista
* MT no determinista

#### Clase P
Contiene aquellos problemas de decisión qeu una MT determinista peude resolver en un tiempo aceptable

#### Clase NP
Contiene problemas de decisión que una MT no determinista puede resolver en tiempo polinomico es decir que es probable que hayan momentos en que no peuda resolver en un tiempo rasonable

### P = NP?
Es un problema que se tiene ya que a medida que avanza la tecnologia problemas NP se han vuelto P ¿Será que llegará el momentoq eu NP=P

## Teoria de la computación
Ciencia rama de la matematica

## Automatas
Maquinas abstractas y problemas que estas son capaces de resolver, los automatas son clasificados a menudo por la clase de lenguajes formales que son capaz de resolver

## Clases de complejidad
* Clase L: Problemas que puden ser resueltos en un espacio log(n)
* Clase NL: Son problemas de decisión que pueden ser resueltos en espacio log(n) sin contar el tamaño de entrada con una maquina de turing no determinista
* Clase NP: Es el conjutno de problemas que pueden ser resueltos en tiempo polinómico por una máquina de turing no determinista . esta clase de problemas tienen muchos problemas de búsqueda y optimización. Es decir que pueden ser P o NP
* Clase NP-Completo: Estos son problemas más dificiles NP, estos problemas es practicamente imposible que pueden llegar a P.


# Función polinomica del problema
se tratará de buscar una función polinomica que modele o identifique la complejidad del algoritmo.

# Notación O
"El algoritmo es O(f(n))": Quiere decir que al aumentar el n´pumero de datos que debe procesar, el tiempo del algoritmo va a crecer, como crece f en relación a n. Es decir que existe una función que logra representar el tiempo de ejecución por medio de cota superior.
## Teoremas Complejidad en el tiempo (temporal)
### Teorema 1
Lo que importa en una complejidad es la forma de la función que está representando, por lo tanto la complejodad de un algoritmo es O(2n) tambien es O(n) ya que tienen misma forma, a pesar de que tengan diferente pendiente.

### Teorema 2:
Si se tienen varias funciones para ejecutar un algoritmo donde se ejecuta una y luego la otra la complejidad de todo el algoritmo es la complejidad del que sea *mayor* Por ejemplo si se tiene una función con O(n) y la otra O(n^2) la complejidad para el algoritmo será O(n^2)

### Teorema 3
En un algoritmo donde se tienen 2 funciones A y B si A por cada ejecución utiliza a B por lo tanto la complejidad será la *multiplicación* de sus complejidades

### Teorema 4

# Complejidad en el espacio
A manera similar al concepto con la complejidad temporal significa que sus requerimientos de memoria aumentan proporcionalmente al problema

## Factores de selección de algoritmo
* La complejidad en el tiempo
* La complejidad en el espacio
* Dificultad de implementación
* El tamaño del problema. En problemas pequeños muchas veces no improtan los factores anteriores

# Ejercicios
* Complejidad de una asignación 
    var = 5
    O(1)
* Complejidad de vari


# Finalidad de la complejidad
Estimar y establecer a un algoritmo sin necesidad de ejecutar estimar su rendimiento.
