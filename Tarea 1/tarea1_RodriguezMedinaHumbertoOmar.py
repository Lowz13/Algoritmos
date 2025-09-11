# ===================================
# Tarea 1 - Apellido, Nombre - Grupo
# ===================================
# EJERCICIO 1

nombre = "humberto"
edad = 20
print("Hola, me llamo ", nombre, "y tengo ", str(edad), " años.")

#Ejemplo de salida

# EJERCICIO 2
for i in range(1,11,1):
    print(5*i)

#Ejemplo de salida

# EJERCICIO 3
# (Explica en 2 líneas cómo funciona el acumulador)
n = 10
acumulador = 0
for i in range(n):
    acumulador += 1
    print(acumulador)

#...

# EJERCICIO 4
for i in range (21):
    if i % 2 == 0:
        print(i)
# ...

# EJERCICIO 5
calificacion = 17
if calificacion == 10:
    print("EXCELENTE")
elif calificacion >= 6:
    print("APROBADO")   
else:
    print("REPROBADO")
# ...
# EJERCICIO 6
edad = 65
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
    
# ...
# EJERCICIO 8
# (Explica qué hace s[::-1])
# ...
# EJERCICIO 9
# ...
# EJERCICIO 10
# ...
# EJERCICIO 11
# ...
# EJERCICIO 12

# ...
# (Ejercicios adicionales opcionales)