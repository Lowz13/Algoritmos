import random as rd

# ============================
def conseguir_llave(alfabetoCifrado,alfabeto, cifrado):
    llave = ''
    for i in alfabeto:
        
        #opciones = alfabetoCifrado.get(letra, '')
        if len(alfabetoCifrado[i]) == 1:
            llave += alfabetoCifrado[i]
        if len(alfabetoCifrado[i]) > 1 and i in cifrado:
            llave += '_'
        if len(alfabetoCifrado[i]) > 1 and not (i in cifrado):
            llave += '?'
       
    return llave


def descifrando(cadena, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    descifrado = ''
    cadena = cadena.lower()
    for letra in cadena:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            descifrado += llave[indice]
        else:
            descifrado += letra
    return descifrado


def descifra_sustitucion(cadena, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    cadena = cadena.lower()
    for letra in cadena:
        if letra in alfabeto:
            indice = llave.index(letra)
            cifrado += alfabeto[indice]
        else:
            cifrado += letra
    return cifrado


# ============================
# DICIONARIO
# ============================
def carga_diccionario(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as arch:
            print(f"Diccionario {ruta} cargado correctamente.")
            return arch.read().split()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return []
    except Exception as e:
        print(f"Error al cargar diccionario: {e}")
        return []


# ============================
# PRIMERAS PALABRAS
# ============================
def coleccion_de_letras(cadena, adicionales, prueba):
    mejoresLetras = []
    contador = 0
    index = []
    
    for i in cadena.split():
        if len(set(i)) < len(i) or len(i) <= 2:
            if i[-1] in '.,!?':
                i = i[:-1]
            if not (i in mejoresLetras):
                index.append(contador)
                mejoresLetras.append(i)
        contador += 1
    mejoresLetras = sorted(mejoresLetras, key=len, reverse=True)[:]

    
    while adicionales:
        extra = cadena.split()[rd.randint(0, contador-1)]
        if extra[-1] in '.,!?':
                extra = extra[:-1]
        if prueba:
            print ('sugerencia:', extra)
        if not (extra in mejoresLetras):
            if prueba:
                print('agregado:', extra)
            mejoresLetras.append(extra)
            adicionales -= 1  
              
    return mejoresLetras

# ============================
# PALABRAS COMPLETAS
# ============================
def palabras_completas(cadena,prueba):
    letras = []
    for i in cadena.split():
        if i[-1] in '.,!?':
            i = i[:-1]
        if prueba:
            print ('sugerencia:', i)
        letras.append(i)
        letras = sorted(letras, key=len, reverse=True)[:]
    return letras



def palabras_adicionales(cadena, adicionales):
    mejoresLetras = coleccion_de_letras(cadena, adicionales)
    return mejoresLetras

# ============================
# PALABRAS REPETIDAS
# ============================
def leer_palabra_repetida(palabra):
    """Encuentra las posiciones de letras repetidas en una palabra."""
    repetidos = []
    letras_vistas = set()
    
    for letra in palabra:
        if palabra.count(letra) > 1 and letra not in letras_vistas:
            posiciones = [i for i, char in enumerate(palabra) if char == letra]
            repetidos.append(posiciones)
            letras_vistas.add(letra)

    return repetidos, len(repetidos) # Devuelve también el conteo de letras repetidas

def buscar_letras():
    posiblesLetras = ['' for i in range(26)]
    return posiblesLetras


#============================
# SUPOSICION
# ============================
def suposicion (alfabetoCifrado,alfabeto, cifrado,prueba):
    for i in alfabeto:
        
        
        #encontrar letras que no terminaron de definirse
        if len(alfabetoCifrado[i]) > 1 and i in cifrado:
            if prueba:
                print("revisando:", i, alfabetoCifrado[i])
                print("="*20)
            temp = alfabetoCifrado[i]
            tempDos = ''
            for compara in alfabeto:
                if len(alfabetoCifrado[compara]) == 1 and alfabetoCifrado[compara] in temp:
                    if prueba:
                        print("encontro coincidencia en:",compara)
                    for j in temp:
                        if j != alfabetoCifrado[compara]:
                            tempDos += j

                    if prueba:
                        print("temporal:", tempDos)
                    temp = tempDos
                    if len(tempDos) == 1:
                        alfabetoCifrado[i] = ''
                        alfabetoCifrado[i] = tempDos
                        break
                    tempDos = ''
        if prueba:
            print(i, alfabetoCifrado[i])

    return alfabetoCifrado


# ============================
# FUNCION PRINCIPAL
# ============================
def inicio_descifrado (diccionario, palabra, alfabetoCifrado, prueba):
    #acumuladores
    coincidencias = 0
    pruebaCoincidencias = ''
    externo = {}
    
    
    #conseguir las letras repetidas
    lector = leer_palabra_repetida(palabra)
    indexLetrasRepetidas = lector[0]
    
    
    # Convertir patrones a pares de posiciones que deben ser iguales
    posiciones_iguales = []
    
    
    for patron_letras in indexLetrasRepetidas:
        # Para cada grupo de letras repetidas (ej: [0,2,4] para 'a')
        # Crear todos los pares posibles
        for i in range(len(patron_letras)):
            for j in range(i + 1, len(patron_letras)):
                posiciones_iguales.append((patron_letras[i], patron_letras[j]))
    
    if prueba:
        print("="*20)
        print(f"Palabra: {palabra}")
        print(f"Posiciones que deben ser iguales: {posiciones_iguales}")
        print("="*20)
    
    
    for limpieza in set(palabra):
        externo[limpieza] = ''
    
        
    for p in diccionario:
        #condicion de longitud y caracteres unicos
        
        if len(p) == len(palabra) and len(set(p)) == len(set(palabra)):
            # Verificar si las letras en las posiciones especificadas son iguales
            # primer filtrado
            if all(p[pos1] == p[pos2] for pos1, pos2 in posiciones_iguales 
                   if pos1 < len(p) and pos2 < len(p)):
                #Segundo filtrado
                for patron in range(len(palabra)):
                    bandera = False
                    if prueba:
                        print('revisando:', p[patron],'en',palabra[patron], alfabetoCifrado[palabra[patron]])
                    if p[patron] in alfabetoCifrado[palabra[patron]]:
                        bandera = True
                        
                    if bandera == False:
                        if prueba:
                            print(p,'no cumple con\n')
                        
                        break
                
                if bandera == True:
                    if prueba:
                        print(p,'\n')
                    coincidencias += 1

                if prueba:
                    print('posible:', p)

                for c in range(len(palabra)):
                    if not (p[c] in externo[palabra[c]]) and bandera == True:
                        externo[palabra[c]] += p[c]


    for c in set(palabra):
        if 1:
            if len(externo[c]) == len(alfabetoCifrado[c]):
                print("iguales",c, alfabetoCifrado[c],'->', externo[c])
            if len(externo[c]) > len(alfabetoCifrado[c]) and coincidencias > 0:
                print("error",c, externo[c], alfabetoCifrado[c])
        
        if len(externo[c]) < len(alfabetoCifrado[c]) and coincidencias > 0:
            
            print("cambios",c, alfabetoCifrado[c],'->', externo[c])
            alfabetoCifrado[c] = externo[c]
            
    

                  
    print('la palabra',palabra,'cumple:', coincidencias)
    print("="*20)
    if coincidencias == 1:
        alfabetoCifrado[c] = externo[c]
    if prueba:
        for i in set(palabra):
            print(i, alfabetoCifrado[i])

    
    
    return alfabetoCifrado, coincidencias


def elimina_completados(coleccion, eliminados):
    for e in eliminados:
        if e in coleccion:
            count = coleccion.count(e)
            for _ in range(count):
                coleccion.remove(e)
    return coleccion

# ============================
def main():
    #Constantes
    ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
    CIFRADO = 'iqzn hdiq l omrn ovncn jle l bianbk dcmqznee. who evn vlf lq nqzvlqornqo hdiq ' \
            'vnc ip l pnlcphb eico jvmzv zihbf iqbk wn wciunq wk bian.'
            
    #Inicializar
    alfabetoCifrado = {letra : ALFABETO for letra in ALFABETO}
    diccionario = carga_diccionario('Tarea 2/words.txt')
    if not diccionario:
        return

    #Proceso
    print("Iniciando proceso de descifrado...")
    
    #Fase 1: palabras con patrones
    coleccion = coleccion_de_letras(CIFRADO,3, False)
    eliminados = []
    print("Coleccion:",coleccion)
    for _ in range(3):
        for palabra in coleccion:
            cifrado = inicio_descifrado(diccionario, palabra, alfabetoCifrado, False)
            alfabetoCifrado = cifrado[0]
            if cifrado[1] == 1 or cifrado[1] == 0:
                print("Palabra resuelta:", palabra)
                eliminados.append(palabra)
        elimina_completados(coleccion, eliminados)
                
        
    for i in ALFABETO:
        print(i, alfabetoCifrado[i])
        
    print("Palabras eliminadas:", eliminados)
    print("="*20)
    
    general = palabras_completas(CIFRADO,False)
    print(general)
    if len(general) == len(CIFRADO.split()):
        print("Se encontraron todas las palabras.")
    elimina_completados(general, eliminados)
    print(general)
    
    for i in range(2):
        for j in range(len(general)):
            cifrado = inicio_descifrado(diccionario, general[j], alfabetoCifrado, False)
            alfabetoCifrado = cifrado[0]
            if cifrado[1] == 1 or cifrado[1] == 0:
                print("Palabra resuelta:", palabra)
                eliminados.append(palabra)
        elimina_completados(coleccion, eliminados)

    alfabetoCifrado = suposicion(alfabetoCifrado, ALFABETO, CIFRADO, False)

    llave = conseguir_llave(alfabetoCifrado, ALFABETO, CIFRADO)
    print("Llave encontrada:")
    print(llave)


    mensaje = descifrando(CIFRADO, llave)
    print("Mensaje descifrado:")
    print("="   *20)
    print(CIFRADO)
    print(mensaje)

if __name__ == "__main__":
    main()
