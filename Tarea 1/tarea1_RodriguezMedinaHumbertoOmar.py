# ===================================
# Tarea 1 - Apellido, Nombre - Grupo
# ===================================
# EJERCICIO 1
# Creamos las variables nombre y edad como int
nombre = "humberto"
edad = 20
# cambiamos el tipo de edad a str para concatenar
print("Hola, me llamo ", nombre, "y tengo ", str(edad), " años.")
#Ejemplo de salida
# Hola, me llamo Humberto y tengo 20 años.

# EJERCICIO 2
#Imprimir los pimeros 
n = 10
for i in range(1, n+1):
    print(5*i)
#Ejemplo de salida
# si n = 5
# 5
# 10
# 15
# 20
# 25

# EJERCICIO 3
# (Explica en 2 líneas cómo funciona el acumulador)
n = 5
acumulador = 0
for i in range(n):
    acumulador += (i+1)
    print('result',acumulador)

print('la suma de 1 a',n,'es',acumulador)
#Ejemplo de salida
# si n = 5
# 1
# 3
# 6
# 10
# 15

# EJERCICIO 4
n = 20
for i in range (n+1):
    if i % 2 == 0:
        print(i)
# Ejemplo de salida
# si n = 10
# 0
# 2
# 4
# 6
# 8
# 10

# EJERCICIO 5
calificacion = 5
if calificacion == 10:
    print("EXCELENTE")
elif calificacion >= 6:
    print("APROBADO")   
else:
    print("REPROBADO")
# Ejemplo de salida
# si calificacion <= 5
# REPROBADO
# si calificacion >= 6 y <= 9
# APROBADO
# si calificacion = 10
# EXCELENTE
# EJERCICIO 6
edad = 64
if edad < 12:
    monto = 30
elif edad >= 12 and edad <= 64:
    monto = 50
else:
    monto = 25
print("Precio: $", monto)
# ...
# EJERCICIO 7
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cadena = "Hola, me llAmo Humberto"
contador = 0
for c in cadena:
    if c in vocales:
        contador += 1
        print("se encontro", c, "el contador es:", contador)
    
print("Total de vocales mayúscuas o minúsculas:", contador)
# ...
# EJERCICIO 8
# (Explica qué hace s[::-1])
#S[los primeros caracteres: los ultimos caracteres: el paso de uno en uno hacia atras]
s = "Humberto"
print(s[::-1])
# ...
# EJERCICIO 9
prohibida = "spoiler"
frase = "¡ALERTA DE SPOILER! Si no has visto la última película de Spiderman, te recomendamos no continuar leyendo."
textoAlt = "este texto no tiene la palabra clave"
if prohibida in frase.lower():
    print("ALERTA")
else:
    print("OK")
# ...
# EJERCICIO 10
numero = 5
palabra = ""
if numero % 3 == 0:
    palabra += "Fizz"
if numero % 5 == 0:
    palabra += "Buzz"
if numero % 3 != 0 and numero % 5 != 0:
    palabra = str(numero)
print(palabra)

# ...
# EJERCICIO 11
piramide = ""
for i in range(10):
    piramide += "#"
    print(piramide)
# ...
# EJERCICIO 12
a = "a"
b = "z"
if a > b:
    print(b, "es el primero alfabeticamente")
elif a < b:
    print(a, "es el primero alfabeticamente")
elif a == b:
    print("son iguales")
# ...
# (Ejercicios adicionales opcionales)
# EJERCICIO 13
n = 11
terPar = ['0','2','4','6','8']
terImpar = ['1','3','5','7','9']
if n % 2 != 0:
    print("Es impar")
else:
    print("Es par")
#...