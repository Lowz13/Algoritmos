import random as rd


# ============================
def conseguir_llave(alfabetoCifrado):
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
    arch = open(ruta, 'r')
    texto = arch.read()
    arch.close()
    return texto.split()


# ============================
# PRIMERAS PALABRAS
# ============================
def coleccion_de_letras(cadena, adicionales):
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
        #print ('sugerencia:', extra)
        if not (extra in mejoresLetras):
            #print('agregado:', extra)
            mejoresLetras.append(extra)
            adicionales -= 1  
              
    return mejoresLetras

# ============================
# PALABRAS COMPLETAS
# ============================
def palabras_completas(cadena):
    letras = []
    for i in cadena.split():
        if i[-1] in '.,!?':
            i = i[:-1]
        #print ('sugerencia:', i)
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
def suposicion (alfabetoCifrado):
    for i in alfabeto:
        
        
        #encontrar letras que no terminaron de definirse
        if len(alfabetoCifrado[i]) > 1 and i in cifrado:
            print("revisando:", i, alfabetoCifrado[i])
            print("="*20)
            temp = alfabetoCifrado[i]
            tempDos = ''
            for compara in alfabeto:
                if len(alfabetoCifrado[compara]) == 1 and alfabetoCifrado[compara] in temp:
                    print("encontro coincidencia en:",compara)
                    for j in temp:
                        if j != alfabetoCifrado[compara]:
                            tempDos += j
                            
                    print("temporal:", tempDos)
                    temp = tempDos
                    if len(tempDos) == 1:
                        alfabetoCifrado[i] = ''
                        alfabetoCifrado[i] = tempDos
                        break
                    tempDos = ''

        print(i, alfabetoCifrado[i])

    return alfabetoCifrado


# ============================
# FUNCION PRINCIPAL
# ============================
def inicio_descifrado (diccionario, palabra, alfabetoCifrado):
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
                    #print('revisando:', p[patron],'en',palabra[patron], alfabetoCifrado[palabra[patron]])
                    if p[patron] in alfabetoCifrado[palabra[patron]]:
                        bandera = True
                        
                    if bandera == False:
                        #print(p,'no cumple con\n')
                        break
                
                if bandera == True:
                    #print(p,'\n')
                    coincidencias += 1

            
                #print('posible:', p)
                #print('posible:', p)
                
                for c in range(len(palabra)):
                    if not (p[c] in externo[palabra[c]]) and bandera == True:
                        externo[palabra[c]] += p[c]


    for c in set(palabra):
        #print (c)
        #if len(externo[c]) == len(alfabetoCifrado[c]):
            #print("iguales",c, externo[c], alfabetoCifrado[c])
        #if len(externo[c]) > len(alfabetoCifrado[c]) and coincidencias > 0:
            #print("error",c, externo[c], alfabetoCifrado[c])
        
        if len(externo[c]) < len(alfabetoCifrado[c]) and coincidencias > 0:
            print("cambios",c, externo[c], alfabetoCifrado[c])
            alfabetoCifrado[c] = externo[c]
        
                  
    print('cumple:', coincidencias)

    for i in set(palabra):
        print(i, alfabetoCifrado[i])

    
    
    return alfabetoCifrado


# ============================
numeros = '0123456789'

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

cifrado = 'iqzn hdiq l omrn ovncn jle l bianbk dcmqznee. who evn vlf lq nqzvlqornqo hdiq ' \
          'vnc ip l pnlcphb eico jvmzv zihbf iqbk wn wciunq wk bian.'
          
#Crear alfabeto cifrado
alfabetoCifrado = {}
for i in alfabeto:
    alfabetoCifrado[i] = alfabeto

diccionario = carga_diccionario('Tarea 2/words.txt')

print("Creando un arreglo de palabras a descirfrar...")
coleccion = coleccion_de_letras(cifrado,3)
print("Coleccion:",coleccion)

for repeticion in range(3):
    for i in range(len(coleccion)):
    #for i in range(3):
        descifraA = inicio_descifrado(diccionario, coleccion[i], alfabetoCifrado)
        alfabetoCifrado = descifraA
for i in alfabeto:
    print(i, alfabetoCifrado[i])

general = palabras_completas(cifrado)
print(general)
if len(general) == len(cifrado.split()):
    print("Se encontraron todas las palabras.")
for i in range(2):
    for j in range(len(general)):
        descifraA = inicio_descifrado(diccionario, general[j], alfabetoCifrado)
        alfabetoCifrado = descifraA

alfabetoCifrado = suposicion(alfabetoCifrado)

llave = conseguir_llave(alfabetoCifrado)
print("Llave encontrada:")
print(llave)


mensaje = descifrando(cifrado, llave)
print("Mensaje descifrado:")
print("="   *20)
print(cifrado)
print(mensaje)
