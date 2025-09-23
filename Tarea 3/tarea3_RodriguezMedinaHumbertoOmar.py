
def calcular_dia(inicio, dias):
    semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return semana[(inicio + dias - 1) % 7]
print(calcular_dia(5, 0))

def visiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return print("Año bisiesto")
    return print("No es año bisiesto")
visiesto(2000)