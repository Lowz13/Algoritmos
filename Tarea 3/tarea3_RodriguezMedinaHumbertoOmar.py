
def calcular_dia(inicio, dias):
    semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    return semana[(inicio + dias) % 7]
print(calcular_dia(5, 2))

def visiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return print("Año bisiesto")
    return print("No es año bisiesto")
visiesto(2000)