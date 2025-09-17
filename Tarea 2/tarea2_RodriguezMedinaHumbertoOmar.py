def cifra_cesar(texto, llave):
    """
    Cifra un texto usando el algoritmo César
    Args:
        texto (str): Texto a cifrar
        llave (int): Desplazamiento (0-25)
    Returns:
        str: Texto cifrado
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    texto = texto.lower()
    for c in texto:
        if c in alfabeto:
            # TODO: Implementar el desplazamiento de caracteres
            # Recordar que el alfabeto es cíclico (después de 'z' viene 'a')
            pass
        else:
            resultado += c
    return resultado

def descifra_cesar(cadena_cifrada, llave):
    # TODO: Implementar descifrado
    # Pista: El descifrado es como cifrar con llave negativa
    pass

def cargar_diccionario(archivo):
    """
    Carga las palabras del diccionario desde un archivo
    Args:
        archivo (str): Ruta del archivo words.txt (palabras ya limpias y
        ordenadas)
    Returns:
        list: Lista de palabras en minúsculas ordenadas alfabéticamente
    """
    with open(archivo, 'r', encoding='utf-8') as file:
        # Leer todo el contenido del archivo
        contenido = file.read()
        # Separar las palabras por espacios (ya están limpias y sin repetir)
        diccionario = contenido.split()
    print(f"Diccionario cargado: {len(diccionario)} palabras")
    return diccionario

def get_aciertos(texto, diccionario):
    """
    Cuenta cuántas palabras del texto están en el diccionario
    Args:
        texto (str): Texto a analizar
        diccionario (set): Conjunto de palabras válidas
    Returns:
        int: Número de palabras encontradas en el diccionario
    """
    aciertos = 0
    # TODO: Separar el texto en palabras y contar las que están en
    # diccionario
    # Normalizar a minúsculas para comparar
    pass
    return aciertos