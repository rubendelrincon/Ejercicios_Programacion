#Ejercicio 1 suma dos aarays elemento por elemento 
import numpy as np


array1 = np.array([1,2,3,4,5])
array2 = np.array([10,20,30,40,50])

resultado = array1 + array2

print(resultado)

#Ejercicio 2: Multiplicar cada elemento de un array por un numero 

array3 = np.array([1,2,3,4,5,6])


resultado = array3 * 3

print(resultado)

#Ejericio 3: Calcular el promedio de un array 

array4 = np.array([2,3,4,5,6,7,8,9,10,11])

promedio = np.mean(array4)

print(promedio)

#Ejericio 4: Filtrar elementos mayores a un valor dado 

array5 = np.array([1,2,30,4,50,6,70,8])

mayores5 = array5[array5 > 5]
print (mayores5)

#Ejercicio 5 : elevar ak cuadrado un elemento de un array 

array6 = np.array([1,2,30,4,50,6,70,8])

elevado2 = array6 ** 2
print (elevado2)