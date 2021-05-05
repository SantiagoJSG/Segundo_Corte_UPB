# Ejercicio 1
import numpy as np
#Asignamos a la variable array 2 filas personalizadas con 4 columnas, conformadas por datos de tipo int64 (enteros de 64 bits)
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int64)
#Imprimimos el Array
print(array)

# Ejercicio 2
import numpy as np
#Asignamos a la variable array 5 filas con 5 columnas, conformadas únicamente por unos
array = np.ones([5, 5])
#Imprimimos el Array
print(array)

# Ejercicio 3
import numpy as np
#Asignamos a la variable array 6 filas con 9 columnas, conformadas únicamente por ceros
array = np.zeros([6, 9])
#Imprimimos el Array
print(array)

# Ejercicio 4
import numpy as np
#Asignamos a la variable array 5 filas con 4 columnas, conformadas por números aleatorios
array = np.random.random([5, 4])
#Imprimimos el Array
print(array)

# Ejercicio 5
import numpy as np
#Asignamos a la variable array 2 filas con 4 columnas vacías
array = np.empty([2, 4])
#Imprimimos el Array
print(array)

# Ejercicio 6
import numpy as np
#Asignamos a la variable array 4 filas con 4 columnas, conformadas únicamente por cuatros
array = np.full([4, 4], 4)
#Imprimimos el Array
print(array)

# Ejercicio 7.1
import numpy as np
#Asignamos a la variable array 1 fila y una columna conformada por números entre el 0 incluyente, hasta el 21 excluyente, avanzando de 2 en 2
array = np.arange(0, 21, 2)
#Imprimimos el Array
print(array)

# Ejercicio 7.2
import numpy as np
#Asignamos a la variable array 1 fila y una columna conformada por 5 números entre el 0 hasta el 5
array = np.linspace(0, 5, 5)
#Imprimimos el Array
print(array)

# Ejercicio 8.1
import numpy as np
#Asignamos a la variable array 5 filas y 4 columnas, en la cual, los elementos en diagonal son igual a 1 y el resto 0
array = np.eye(5, 4)
#Imprimimos el Array
print(array)

# Ejercicio 8.2
import numpy as np
#Asignamos a la variable array 5 filas y 5 columnas, en la cual, los elementos en diagonal son igual a 1 y el resto 0
array = np.identity(5)
#Imprimimos el Array
print(array)
