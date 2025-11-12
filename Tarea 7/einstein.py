"""
VERSIÓN 1: SIN OPTIMIZACIONES
Todas las condiciones se evalúan al final.
Genera TODAS las combinaciones posibles primero.
"""

import time
import itertools

from pyparsing import col

colores = ['roja', 'verde', 'blanca', 'amarilla', 'azul']
nacionalidades = [ 'danes', 'britanico', 'sueco',
'aleman']
bebidas = ['agua', 'te', 'cafe', 'cerveza']
cigarros = ['pall_mall', 'dunhill', 'blends', 'blue_master',
'prince']
mascotas = ['perros', 'pajaros', 'gatos', 'caballos', 'peces']

def vecinos(pos1, pos2):
    """Verifica si dos posiciones son vecinas"""
    return abs(pos1 - pos2) == 1

def cumple_condiciones(col, nac, beb, cig, mas):
    """
    Verifica TODAS las condiciones del acertijo.
    Retorna True si la combinación es válida.
    """
    
    # Restricción 1: El británico vive en la casa roja
    for i in range(5):
        if nac[i] == 'britanico' and col[i] != 'roja':
            return False
        if col[i] == 'roja' and nac[i] != 'britanico':
            return False
        
    # Restricción 2: El sueco tiene perros
    for i in range(5):
        if nac[i] == 'sueco' and mas[i] != 'perros':
            return False
        if mas[i] == 'perros' and nac[i] != 'sueco':
            return False
        
    # Restricción 3: El danés toma té
    for i in range(5):
        if nac[i] == 'danes' and beb[i] != 'te':
            return False
        if beb[i] == 'te' and nac[i] != 'danes':
            return False
        
    # Restricción 4: La casa verde está a la izquierda de la blanca
    verde_pos = col.index('verde')
    blanca_pos = col.index('blanca')
    if verde_pos != blanca_pos - 1:
        return False
    
    # Restricción 5: El dueño de la casa verde toma café
    if beb[verde_pos] != 'cafe':
        return False
    
    # Restricción 6: La persona que fuma Pall Mall tiene pájaros
    for i in range(5):
        if cig[i] == 'pall_mall' and mas[i] != 'pajaros':
            return False
        if mas[i] == 'pajaros' and cig[i] != 'pall_mall':
            return False
    # Restricción 7: El dueño de la casa amarilla fuma Dunhill
    for i in range(5):
        if col[i] == 'amarilla' and cig[i] != 'dunhill':
            return False
        if cig[i] == 'dunhill' and col[i] != 'amarilla':
            return False
        
    # Restricción 8: El que vive en la casa del centro toma leche
    if beb[2] != 'leche':
        return False
    # Restricción 9: El noruego vive en la primera casa
    if nac[0] != 'noruego':
        return False
    # Restricción 10: El que fuma Blends vive al lado del que tiene gatos
    blends_pos = cig.index('blends')
    tiene_vecino_gatos = False
    for i in range(5):
        if mas[i] == 'gatos' and vecinos(i, blends_pos):
            tiene_vecino_gatos = True
            break
    if not tiene_vecino_gatos:
        return False
    # Restricción 11: El que tiene caballos vive al lado del que fuma Dunhill
    caballos_pos = mas.index('caballos')
    dunhill_pos = cig.index('dunhill')
    if not vecinos(caballos_pos, dunhill_pos):
        return False

    # Restricción 12: El que fuma Blue Master toma cerveza
    for i in range(5):
        if cig[i] == 'blue_master' and beb[i] != 'cerveza':
            return False
        if beb[i] == 'cerveza' and cig[i] != 'blue_master':
            return False

    # Restricción 13: El alemán fuma Prince
    for i in range(5):
        if nac[i] == 'aleman' and cig[i] != 'prince':
            return False
        if cig[i] == 'prince' and nac[i] != 'aleman':
            return False

    # Restricción 14: El noruego vive al lado de la casa azul
    noruego_pos = nac.index('noruego')
    tiene_vecino_azul = False
    for i in range(5):
        if col[i] == 'azul' and vecinos(i, noruego_pos):
            tiene_vecino_azul = True
            break
    if not tiene_vecino_azul:
        return False

    # Restricción 15: El que fuma Blends tiene un vecino que toma agua
    tiene_vecino_agua = False
    for i in range(5):
        if beb[i] == 'agua' and vecinos(i, blends_pos):
            tiene_vecino_agua = True
            break
    if not tiene_vecino_agua:
        return False

    # Si pasó todas las restricciones
    return True
def mostrar_solucion(col, nac, beb, cig, mas, num_solucion):
    """Muestra la solución en formato tabla"""
    print(f"\n=== SOLUCIÓN {num_solucion} ===")
    print("Casa | Color | Nacionalidad | Bebida | Cigarro | Mascota")
    print("-" * 75)
    for i in range(5):
        print(f"{i+1:4} | {col[i]:8} | {nac[i]:12} | {beb[i]:7} | {cig[i]:11} | {mas[i]:8}")

# Respuesta a la pregunta
    for i in range(5):
        if mas[i] == 'peces':
            print(f"\n¡El {nac[i]} tiene los PECES!")

# PROGRAMA PRINCIPAL
print("Generando todas las combinaciones posibles...")
inicio = time.time()
combo_col = [('amarilla', 'azul','roja', 'verde', 'blanca')]
#combo_col = list(itertools.permutations(colores))
combo_nac = list(itertools.permutations(nacionalidades))
combo_beb = list(itertools.permutations(bebidas))
combo_cig = list(itertools.permutations(cigarros))
combo_mas = list(itertools.permutations(mascotas))
print(f"Colores: {len(combo_col)} combinaciones")
print(f"Nacionalidades: {len(combo_nac)} combinaciones")
print(f"Bebidas: {len(combo_beb)} combinaciones")
print(f"Cigarros: {len(combo_cig)} combinaciones")
print(f"Mascotas: {len(combo_mas)} combinaciones")
print(f"Total a probar: {len(combo_col) * len(combo_nac) *
len(combo_beb) * len(combo_cig) * len(combo_mas):,}")
print("\nBuscando soluciones...\n")
soluciones = 0
combinaciones_probadas = 0
# Probar TODAS las combinaciones
for col in combo_col:
    for nac_tail in combo_nac:
        nac=('noruego',) + nac_tail # Fijar noruego en la primera casa
        for beb_tail in combo_beb:
            beb = beb_tail[:2] + ('leche',) + beb_tail[2:] # Fijar leche en la casa del medio
            for cig in combo_cig:
                 # Fijar Dunhill en la segunda casa
                for mas in combo_mas:
                    # Fijar caballos en la casa del medio
                    combinaciones_probadas += 1
                    # Evaluar todas las condiciones
                    if cumple_condiciones(col, nac, beb, cig, mas):
                        soluciones += 1
                        mostrar_solucion(col, nac, beb, cig, mas, soluciones)
fin = time.time()
print(f'\n{"="*75}')
print(f'Combinaciones probadas: {combinaciones_probadas:,}')
print(f'Soluciones encontradas: {soluciones}')
print(f'Tiempo total: {fin-inicio:.4f} segundos')
print(f'{"="*75}')