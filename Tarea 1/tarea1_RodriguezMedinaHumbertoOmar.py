# ===================================
# Tarea 1 - Rodriguez Medina, Humberto Omar - 1507
# ===================================

# EJERCICIO 1
# Paso 1: Creamos las variables nombre (string) y edad (int)
# Paso 2: Imprimimos el texto y cambiamos el tipo de edad a str para concatenar
nombre = "humberto"
edad = 20
print("Hola, me llamo ", nombre, "y tengo ", str(edad), " años.")
# Ejemplo de salida
# Hola, me llamo Humberto y tengo 20 años.

# EJERCICIO 2
# Paso 1: Usamos una variable n para definir el rango del ciclo for
# Paso 2: iniciamos desde el numero uno, y le
#         agregamos 1 a n en el rango para que incluya el numero n
# Paso 3: Multiplicamos i por 5 para obtener los primeros n multiplos de 5
n = 10
# Recorremos desde 1 hasta n+1 para incluir n
for i in range(1, n + 1):
    print(5 * i)
# Ejemplo de salida
# si n = 5
# 5
# 10
# 15
# 20
# 25

# EJERCICIO 3
# Paso 1: Usamos una variable n para definir el rango del ciclo for
# Paso 2: iniciamos desde el numero uno, y le agregamos 1 a n en el rango
#         para que incluya el numero n
# Paso 3: Usamos un acumulador que inicia en 0 y en cada iteracion
#         suma el valor de i al valor previo del acumulador
# Paso 4: Al finalizar el ciclo, imprimimos el resultado final del acumulador
n = 10
acumulador = 0
# Recorremos desde 0 hasta n-1, por eso se suma i + 1
for i in range(1, n + 1):
    # acumulador = acumulador + i usando el valor previo y sumando i
    acumulador += i
    print(acumulador)
# Muestra la suma del acumulador
print("la suma de 1 a", n, "es", acumulador)
# Ejemplo de salida
# si n = 5
# 1
# 3
# 6
# 10
# 15

# EJERCICIO 4
# Paso 1: Usamos una variable n para definir el rango del ciclo for
# Paso 2: iniciamos desde el numero cero, y le agregamos 1 a n
#         en el rango para que incluya el numero n
# Paso 3: Usamos una condicion if para imprimir solo los numeros pares

n = 20
for i in range(n + 1):
    # si el residuo de i entre 2 es 0, es par
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
# Paso 1: Usamos una variable calificacion para definir la calificacion
# Paso 2: Usamos una estructura if, elif, else para definir los rangos
#         y mostrar el mensaje correspondiente
calificacion = 5
if calificacion == 10:
    print("EXCELENTE")
    # Ejemplo de salida
    # EXCELENTE
elif calificacion >= 6:
    print("APROBADO")
    # Ejemplo de salida
    # APROBADO
else:
    print("REPROBADO")
    # Ejemplo de salida
    # REPROBADO
    
# EJERCICIO 6
# Paso 1: Usamos una variable edad para definir la edad
# Paso 2: Usamos una estructura if, elif, else para definir los rangos
#         y obtener el valor de la variable monto
# Paso 3: Imprimimos la palabra concatenando el valor de monto
edad = 64
# Se define el monto segun el rango de edad
if edad < 12:
    monto = 30
elif edad >= 12 and edad <= 64:
    monto = 50
else:
    monto = 25
print("Precio: $", monto)
# Ejemplo de salida
# si edad = 10
#     Precio: $ 30

# EJERCICIO 7
# Paso 1: Creamos una lista con las vocales mayusculas y minusculas
# Paso 2: Recorremos la cadena con un ciclo for
# Paso 3: Usamos una condicion if para verificar si el caracter
#         esta en la lista vocales
# Paso 4: Si se encuentra, se incrementa el contador hasta terminar
#         el ciclo
# Paso 5: Imprimimos el total de vocales encontradas
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
cadena = "Hola, me llAmo Humberto"
contador = 0
# Recorremos cada caracter en la cadena
for c in cadena:
    # Si el caracter esta en la lista de vocales, incrementamos el contador
    if c in vocales:
        contador += 1
        #print("se encontro", c, "el contador es:", contador)

print("Total de vocales mayúsculas o minúsculas:", contador)
# Ejemplo de salida
# si cadena = "YO soy Una cadEna" 
# Total de vocales mayúsculas o minúsculas: 7

# EJERCICIO 8
# (Explica qué hace s[::-1])
# Paso 1: La variable s contiene una cadena de texto
# Paso 2: imprimimos la variable s[::-1] con los corchetes para invertir la cadena
# Explicación de la sintaxis:
# s[deja n+1 letras del inicio:quita n+1 letras del inicio:pasos hacia atras (negativo)]
# Si no se especifican los primeros 2, toma toda la cadena
s = "Humberto"
print(s[::-1])
# Ejemplo de salida
# otrebmuH

# EJERCICIO 9
# Paso 1: Definimos la palabra prohibida y la frase a evaluar
# Paso 2: Usamos una condicion if para verificar si la palabra esta en la frase
#         usando .lower() para evitar problemas con mayusculas o minusculas
# Paso 3: Si se encuentra, se imprime "ALERTA", si no, "OK"
prohibida = "spoiler"
frase = "¡ALERTA DE SPOILER! Si no has visto la última película de Spiderman, te recomendamos no continuar leyendo."
textoAlt = "este texto no tiene la palabra clave"
# Checamos si la palabra prohibida esta en la frase
# frase.lower() convierte toda la frase a minusculas para evitar problemas con mayusculas
if prohibida in frase.lower():
    print("ALERTA")
else:
    print("OK")
# ejemplo de salida
# si frase = "¡ALERTA DE SPOILER! Si no has visto la última película de Spiderman, te recomendamos no continuar leyendo."
# ALERTA

# si frase = "este texto no tiene la palabra clave"
# OK

# EJERCICIO 10
# Paso 1: Definimos la variable numero y una variable palabra vacia
# Paso 2: Usamos condiciones if para verificar si el numero es multiplo de
#         3, 5 o ambos, y concatenamos la palabra correspondiente
# Paso 3: Si no es multiplo de ninguno, asignamos el numero a palabra
# Paso 4: Imprimimos el resultado
numero = 5
palabra = ""
# Verificamos si el numero es multiplo de 3, 5 o ambos
if numero % 3 == 0:
    # Si es multiplo de 3, agregamos "Fizz" a palabra
    palabra += "Fizz"
if numero % 5 == 0:
    # Si es multiplo de 5, agregamos "Buzz" a palabra
    palabra += "Buzz"
if numero % 3 != 0 and numero % 5 != 0:
    palabra = numero
print(palabra)
# Ejemplo de salida
# si numero = 3
# Fizz
# si numero = 5
# Buzz
# si numero = 15
# FizzBuzz
# si numero = 7
# 7

# EJERCICIO 11
# Paso 1: Usamos una variable niveles para definir la altura
# Paso 2: Usamos un ciclo for para imprimir los niveles
#         desde 1 hasta niveles+1 para incluir el ultimo nivel
# Paso 3: En cada iteracion imprimimos el caracter "#" multiplicado por el
#         numero de la iteracion i
niveles = 10
for i in range(1,niveles+1):
    #imprime el caracter "#" i veces
    print("#"*i)
# Ejemplo de salida
# si niveles = 5
# #
# ##
# ###
# ####
# #####

# EJERCICIO 12
# Paso 1: Definimos las variables a y b con las letras a comparar
# Paso 2: Usamos una estructura if, elif, else para comparar las letras
#         y mostrar el mensaje correspondiente
# Paso 3: Imprimimos el resultado
a = "a"
b = "z"
# Compara las letras y muestra el primero alfabeticamente
if a > b:
    print(b, "es el primero alfabeticamente")
elif a < b:
    print(a, "es el primero alfabeticamente")
elif a == b:
    print("son iguales")
# Ejemplo de salida
# si a = "a" y b = "z"
# a es el primero alfabeticamente
# si a = "z" y b = "a"
# a es el primero alfabeticamente
# si a = "b" y b = "b"
# son iguales

# (Ejercicios adicionales opcionales)

n = 11
terPar = ["0", "2", "4", "6", "8"]
terImpar = ["1", "3", "5", "7", "9"]
if n % 2 != 0:
    print("Es impar")


n = 10
for i in range(1, n + 1):
    print (i * i)

frase = "anita lava la tina"
espacio = " "
contador = 0
for i in frase:
    if i in espacio:
        contador += 1
print("Total de espacios:", contador)  


cadena = "Hola soy German Garmendia"
print (cadena[:-1:])


palabra = "PY"
add = "*" + palabra + "*"
print ("*" * (len(add)))
print (add)
print ("*" * (len(add)))

for i in range(10, 0, -1):
    print(i)

edad = 12
if edad < 12:
    print("niño")
elif edad >= 12 and edad < 18:
    print("adolescente")
elif edad >= 18 and edad < 65:
    print("adulto")
else:
    print("mayor")
    
cadena = "anita lava la tina"
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",]
contador = 0
for c in cadena:
    if c in consonantes:
        contador += 1
print("Total de consonantes:", contador)
