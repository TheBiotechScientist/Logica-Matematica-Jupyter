# Librerías: Colección de comandos o funciones.
# se manda llamar a la librería con el comando "import"
#%% 
import math
import numpy
#%%
x = 24
print(numpy.absolute(x))
print(not(x))

# print(math.sqrt(x))
print(math.log(x))
# %pip install logic
# %%
### Comentarios
    # Este es un comentario
    # Este es otro comentario
    # No afecta a los comandos
    # No se ejecuta
    # Sirven para comentar alguna línea
# (P no -> ^ Q)

print("Hola mundo de nuevo") # Este comando imprime en la pantalla

## Veamos los tipos de datos:
# Tipo int = entero:
5 # dato entero
1000 # dato entero
5.5
# Bool

# Tipo de dato str = string = cadena de texto
print("Esta es una cadena de texto")
print(1000)

# Mostrar el tipo de dato:
# print(type("Cadena de texto")) # type nos muestra el tipo de dato
# print(type(1000))

## Variables: 
# Es un objeto al que se le asigna un tipo de dato, o varios tipos de datos
        # Regla: No deben empezar con número
        # 7años = "Siete años" X

X = "Mi nombre es "

print(X)

X = "Ya no tengo nombre"

print(X)


Vacio_completo = "No es cierto, si hay algo"

variableX = "Mi nombre es "
variableY = "Javier"
variableZ = "Karen"
variable1 = 5
variable2 = 20
mi_edad = ", yo tengo "


edad = 36
print("Tipo de dato de edad: ", type(edad))

edad = str(edad)
print("Muestrame el nuevo tipo de dato de edad: ",type(edad))

edad = edad + 20

unidad_edad = " años"

todo_junto = variableX + variableY + mi_edad + unidad_edad

print(variableX, variableY, mi_edad, edad, unidad_edad)

## Comando str(): Convierte un dato tipo int a tipo str
print(str(edad))

print(variableX + variableY + mi_edad + str(edad) + unidad_edad)

