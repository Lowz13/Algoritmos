import tkinter as tk
import random
import math
import time
import itertools

class Ciudad:
    def __init__(self, nombre, xpos, ypos):
        self.nombre = nombre
        self.xpos = xpos
        self.ypos = ypos

def distancia_entre_ciudades(ciudad1, ciudad2):
    dx = ciudad1.xpos - ciudad2.xpos
    dy = ciudad1.ypos - ciudad2.ypos
    return math.sqrt(dx**2 + dy**2)

def get_costo_ruta(ciudades, ruta):
    costo = 0
    for i in range(len(ruta) - 1):
        costo += distancia_entre_ciudades(ciudades[ruta[i]], ciudades[ruta[i+1]])
    costo += distancia_entre_ciudades(ciudades[ruta[-1]], ciudades[ruta[0]])  # regreso al inicio
    return costo

def get_ruta_optima(ciudades):
    indices = list(range(len(ciudades)))
    rutas = itertools.permutations(indices)
    mejor_ruta = None
    menor_costo = float('inf')
    for ruta in rutas:
        costo = get_costo_ruta(ciudades, ruta)
        if costo < menor_costo:
            menor_costo = costo
            mejor_ruta = ruta
    return mejor_ruta

def get_ruta_aleatoria(ciudades, num_intentos):
    mejor_costo = float('inf')
    mejor_ruta = None
    indices = list(range(len(ciudades)))
    for _ in range(num_intentos):
        ruta = random.sample(indices, len(indices))  # permutación aleatoria
        costo = get_costo_ruta(ciudades, ruta)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_ruta = ruta
    return mejor_ruta

def dibuja_ruta(ciudades, ruta):
    canvas.delete("all")
    for ciudad in ciudades:
        canvas.create_oval(ciudad.xpos-5, ciudad.ypos-5, ciudad.xpos+5, ciudad.ypos+5, fill="red")
        canvas.create_text(ciudad.xpos+10, ciudad.ypos, text=ciudad.nombre, anchor="w")
    for i in range(len(ruta)):
        c1 = ciudades[ruta[i]]
        c2 = ciudades[ruta[(i+1)%len(ruta)]]
        canvas.create_line(c1.xpos, c1.ypos, c2.xpos, c2.ypos, fill="blue", width=2)

def resolver_optimo():
    inicio = time.time()
    ruta = get_ruta_optima(ciudades)
    fin = time.time()
    costo = get_costo_ruta(ciudades, ruta)
    dibuja_ruta(ciudades, ruta)
    label_costo_optimo.config(text=f"Costo ruta óptima: {costo:.2f} (tiempo: {fin-inicio:.2f}s)")

def resolver_aleatorio():
    try:
        intentos = int(entry_intentos.get())
        if intentos <= 0:
            raise ValueError
    except ValueError:
        label_costo_aleatorio.config(text="Número de intentos inválido")
        return
    inicio = time.time()
    ruta = get_ruta_aleatoria(ciudades, intentos)
    fin = time.time()
    costo = get_costo_ruta(ciudades, ruta)
    dibuja_ruta(ciudades, ruta)
    label_costo_aleatorio.config(
        text=f"Costo ruta aleatoria: {costo:.2f} con {intentos} intentos (tiempo: {fin-inicio:.2f}s)"
    )



def generar_ciudades():
    global ciudades
    try:
        nuevo_n = int(entry_n.get())
        if nuevo_n < 3:
            raise ValueError
    except ValueError:
        label_costo_optimo.config(text="Número de ciudades inválido (mínimo 3)")
        return
    ciudades = []
    for c in range(nuevo_n):
        ciudades.append(Ciudad(str(c), random.randint(50, 450), random.randint(50, 450)))
    canvas.delete("all")
    for ciudad in ciudades:
        canvas.create_oval(ciudad.xpos-5, ciudad.ypos-5, ciudad.xpos+5, ciudad.ypos+5, fill="red")
        canvas.create_text(ciudad.xpos+10, ciudad.ypos, text=ciudad.nombre, anchor="w")
    label_costo_optimo.config(text="Costo ruta óptima: ---")
    label_costo_aleatorio.config(text="Costo ruta aleatoria: ---")

def get_solucion_cercanos(ciudades):
    pass

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Problema del Agente Viajero")

canvas = tk.Canvas(ventana, width=500, height=500, bg="white")
canvas.pack()

frame_controles = tk.Frame(ventana)
frame_controles.pack(pady=10)

# Número de ciudades
tk.Label(frame_controles, text="Número de ciudades:").grid(row=0, column=0, padx=5)
entry_n = tk.Entry(frame_controles, width=5)
entry_n.grid(row=0, column=1)
entry_n.insert(0, "11")

boton_generar = tk.Button(frame_controles, text="Generar ciudades", command=generar_ciudades)
boton_generar.grid(row=0, column=2, padx=10)

# Botón fuerza bruta
boton_optimo = tk.Button(frame_controles, text="Resolver por fuerza bruta", command=resolver_optimo)
boton_optimo.grid(row=1, column=0, columnspan=2, pady=5)

label_costo_optimo = tk.Label(frame_controles, text="Costo ruta óptima: ---")
label_costo_optimo.grid(row=1, column=2, padx=5)

# Número de intentos aleatorios
tk.Label(frame_controles, text="Intentos aleatorios:").grid(row=2, column=0, padx=5)
entry_intentos = tk.Entry(frame_controles, width=10)
entry_intentos.grid(row=2, column=1)
entry_intentos.insert(0, "1000")

boton_aleatorio = tk.Button(frame_controles, text="Ruta aleatoria", command=resolver_aleatorio)
boton_aleatorio.grid(row=2, column=2, padx=5)

label_costo_aleatorio = tk.Label(frame_controles, text="Costo ruta aleatoria: ---")
label_costo_aleatorio.grid(row=3, column=0, columnspan=3, pady=5)

# Inicializar con ciudades por defecto
ciudades = []
for c in range(int(entry_n.get())):
    ciudades.append(Ciudad(str(c), random.randint(50, 450), random.randint(50, 450)))
for ciudad in ciudades:
    canvas.create_oval(ciudad.xpos-5, ciudad.ypos-5, ciudad.xpos+5, ciudad.ypos+5, fill="red")
    canvas.create_text(ciudad.xpos+10, ciudad.ypos, text=ciudad.nombre, anchor="w")

ventana.mainloop()
