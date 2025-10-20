import random as rd
import time 

class Cosas():
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        
def evalua(num, arregloCosas, restriccion):
    ganancia = 0
    peso = 0
    cad = bin(num)
    cad = cad[2:]
    cad = cad.zfill(len(arregloCosas))
   # print(cad)
    for c in range(len(cad)):
        if cad[c] == '1' and c < len(arregloCosas):
            #print(arregloCosas[c].nombre, arregloCosas[c].precio, arregloCosas[c].peso)
            ganancia += arregloCosas[c].precio
            peso += arregloCosas[c].peso
    if peso > restriccion:
        return -1
    else:
        return ganancia, peso
    
    
inicio = time.time()
saco=[]
#10000000 otro 0 y ya no funciona la compu
for i in range(10000000):
    saco.append(Cosas("objeto"+str(i), rd.randint(50,200), rd.randint(1,20)))
    pass
tiempo_creacion = time.time()
print(f"Tiempo de creación del saco: {tiempo_creacion - inicio:.2f} segundos")

print(evalua(255, saco, 99999999999999999999))
tiempo_total = time.time()
print(f"Tiempo total: {tiempo_total - inicio:.2f} segundos")
print(f"Tiempo de evaluación: {tiempo_total - tiempo_creacion:.2f} segundos")