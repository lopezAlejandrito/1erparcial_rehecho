from random import randint
import os
import csv
import json

##############################
###########PUNTO 1############
##############################
def get_path_actual(nombre_archivo):
    """
    Retorna la ruta completa de un archivo dado su nombre en el directorio actual del script.

    Parameters:
    nombre_archivo : str
        Nombre del archivo cuya ruta se desea obtener.

    Returns:
    str
        Ruta completa del archivo en el directorio actual del script.

    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_csv():
    """
    Carga un archivo CSV de bicicletas y devuelve una lista de diccionarios con los datos.

    La función solicita al usuario ingresar el nombre del archivo CSV. Utiliza la función
    get_path_actual(nombre_archivo) para obtener la ruta completa del archivo en el directorio actual del script.
    Lee el archivo CSV, convierte cada línea en un diccionario con las siguientes claves:
    'id_bike', 'nombre', 'tipo' y 'tiempo', luego devuelve una lista de estos diccionarios.

    Returns:
    -------
    list
        Lista de diccionarios donde cada diccionario representa una bicicleta con sus atributos.
        Si ocurre algún error durante la carga (como archivo no encontrado o formato incorrecto),
        devuelve una lista vacía y muestra un mensaje de error.

    """
    archivo_nombre = input('Ingrese nombre del archivo CSV: ')
    archivo_ruta = get_path_actual(archivo_nombre)
    lista_de_bicicletas = []

    try:
        with open(archivo_ruta, 'r') as archivo:
            encabezado = archivo.readline().strip('\n').split(',')

            lineas = archivo.readlines()
            for linea in lineas:
                bicicleta = {}
                linea = linea.strip('\n').split(',')
                id_bike, nombre, tipo, tiempo = linea

                bicicleta['id_bike'] = int(id_bike)
                bicicleta['nombre'] = nombre
                bicicleta['tipo'] = tipo
                bicicleta['tiempo'] = float(tiempo)
                lista_de_bicicletas.append(bicicleta)
        print('El archivo fue correctamente cargado.')
        return lista_de_bicicletas
    except FileNotFoundError:
        print(f"Error: No se encuentra'{archivo_nombre}'.")
        return []
    
    except Exception as e:
        print(f'Error: {e}')
        return []


def cartel_menu():
    print('------------------------------------------------')
    print('----------------------MENÚ---------------------')
    print('------------------------------------------------')

def opciones_menu(*args)->str:
    """
    Genera un menú de opciones enumeradas a partir de una lista de argumentos.

    Parameters:
    *args : str
        Una lista de opciones para el menú. Cada opción debe ser una cadena de texto.

    Returns:
    str
        Una cadena de texto que representa el menú con las opciones enumeradas.

    Raises:
    ValueError
        Si no se proporcionan opciones, se lanza un error indicando que debe haber al menos una opción para el menú.
    """
    if len(args) == 0:
        raise ValueError('Debe haber al menos una opción para el menú')
    
    menu_opciones = '\n'
    for i, opcion in enumerate(args, start=1):
        menu_opciones += f"{i}. {opcion}\n"
    
    return menu_opciones


##############################
###########PUNTO 2############
##############################

def mostrar_bicicleta_fila(bicicleta:dict):
    """
    Imprime la información de una bicicleta en una fila formateada.

    Parameters:
    bicicleta : dict
        Un diccionario que contiene la información de la bicicleta. Se espera que tenga las siguientes claves:
        - 'id_bike': Identificador único de la bicicleta.
        - 'nombre': Nombre del dueño de la bicicleta.
        - 'tipo': Tipo de bicicleta (por ejemplo, 'BMX', 'PLAYERA', etc.).
        - 'tiempo': Tiempo asociado a la bicicleta en minutos.

    Returns:
    None
    """
    print(f'{bicicleta["id_bike"]:^10}{bicicleta["nombre"]:^10}{bicicleta["tipo"]:^10}{bicicleta["tiempo"]:^10}')

def imprimir_lista_de_bicicletas(lista_de_bicicletas)->None:
    """
    Imprime una lista de bicicletas en formato de tabla.

    Parameters:
    lista_de_bicicletas : list of dict
        Una lista de diccionarios, donde cada diccionario contiene la información de una bicicleta. 
        Cada diccionario debe tener las siguientes claves:
        - 'id_bike': Identificador único de la bicicleta.
        - 'nombre': Nombre del dueño de la bicicleta.
        - 'tipo': Tipo de bicicleta (por ejemplo, 'BMX', 'PLAYERA', etc.).
        - 'tiempo': Tiempo asociado a la bicicleta en minutos.

    Returns:
    None
        Esta función no devuelve ningún valor. Imprime directamente la lista de bicicletas en la consola.
    """
    print('----------------------------------------------------------')
    print('              ***LISTA DE PARTICIPANTES***            ')
    print('----------------------------------------------------------')
    print(' ID BIKE    Nombre    Tipo    Tiempo(minutos)   ')
    print('----------------------------------------------------------')

    for bicicleta in lista_de_bicicletas:
        mostrar_bicicleta_fila(bicicleta)
##############################
###########PUNTO 3############
##############################
def mapear_lista_asignar_tiempo(lista:list)->list:
    """
    Asigna un tiempo aleatorio a cada bicicleta en la lista y devuelve una lista con los tiempos asignados.

    Parameters:
    lista : list of dict
        Una lista de diccionarios, donde cada diccionario representa una bicicleta. 
        Cada diccionario debe tener al menos las claves 'id_bike', 'nombre', y 'tipo'.

    Returns:
    list
        Una lista de enteros que representan los tiempos asignados a cada bicicleta, en el mismo orden en que aparecen en la lista original.
    """
    lista_retorno = []
    for bicicleta in lista:
        bicicleta['tiempo'] = randint(50, 120)
        lista_retorno.append((bicicleta)['tiempo'])
    return lista_retorno

##############################
###########PUNTO 4############
##############################

def calcular_menor(tiempo_lista: list) -> int:
    """
    Calcula el menor valor de una lista de tiempos.

    Parameters:
    tiempo_lista : list of int
        Una lista de enteros que representan tiempos en minutos.

    Returns:
    int
        El menor valor de la lista de tiempos.

    Raises:
    ValueError
        Si la lista está vacía o si el argumento proporcionado no es una lista.
    """
    if isinstance(tiempo_lista, list):
        if len(tiempo_lista) == 0:
            raise ValueError('La lista está vacía')
        menor = tiempo_lista[0]
        for tiempo in tiempo_lista:
            if tiempo < menor:
                menor = tiempo
        return menor
    raise ValueError('No es una lista válida')

def informar_ganador(lista: list)->dict:
    """
    Informa el nombre del ganador o los empates basado en el tiempo más bajo en una lista de bicicletas.

    Parameters:
    lista : list of dict
        Una lista de diccionarios que contienen la información de cada bicicleta.
        Cada diccionario debe contener al menos las claves 'nombre' y 'tiempo'.

    Returns:
    dict
        Una lista de diccionarios con los nombres y tiempos de los ganadores (en caso de empate).

    Raises:
    ValueError
        Si la lista está vacía o si alguno de los diccionarios no contiene las claves 'nombre' o 'tiempo'.
    """
    menor_tiempo = calcular_menor([bicicleta['tiempo'] for bicicleta in lista])

    ganadores = []
    for bicicleta in lista:
        if bicicleta['tiempo'] == menor_tiempo:
            ganadores.append({'nombre': bicicleta['nombre'], 'tiempo': bicicleta['tiempo']})
    
    if len(ganadores) == 1:
        print(f"El ganador es {ganadores[0]['nombre']} con un tiempo de {ganadores[0]['tiempo']} minutos.")
    else:
        print("Hubo un empate entre las siguientes bicicletas:")
        for ganador in ganadores:
            print(f"{ganador['nombre']} con un tiempo de {ganador['tiempo']} minutos.")
    
    return ganadores

##############################
###########PUNTO 5############
##############################

def pedir_tipo_de_bicicleta_filtrar():
    """
    Solicita al usuario ingresar el tipo de bicicleta que desea filtrar.

    El usuario debe ingresar uno de los siguientes tipos: 'BMX', 'PLAYERA', 'MTB' o 'PASEO'.
    El ingreso del usuario se valida para asegurarse de que sea uno de los tipos válidos.

    Returns:
    str
        El tipo de bicicleta ingresado por el usuario en mayúsculas ('BMX', 'PLAYERA', 'MTB' o 'PASEO').
    """
    tipo_de_bicicleta = input('Ingresa el tipo de bicicleta que quieres filtrar: ')
    while tipo_de_bicicleta.upper() not in ['BMX', 'PLAYERA', 'MTB', 'PASEO']:
        tipo_de_bicicleta = input('Tipo inválido. Reingresa el tipo de bicicleta que quieres filtrar: ')
    tipo_de_bicicleta = tipo_de_bicicleta.upper()
    return tipo_de_bicicleta

def filtrar_bicicletas(lista: list, tipo)->list:
    """
    Filtra bicicletas de una lista basado en un tipo específico.

    Parameters:
    lista : list of dict
        Una lista de diccionarios, donde cada diccionario representa información de una bicicleta.
        Cada diccionario debe contener al menos la clave 'tipo'.

    tipo : str
        El tipo de bicicleta por el cual se desea filtrar. Debe ser uno de los siguientes valores:
        'BMX', 'PLAYERA', 'MTB', o 'PASEO'.

    Returns:
    list
        Una lista de diccionarios que representan las bicicletas filtradas del tipo especificado.
        Si no se encuentran bicicletas del tipo dado, devuelve una lista vacía.
    """

    lista_retorno = []
    for bicicleta in lista:
        if bicicleta['tipo'] == tipo:
            lista_retorno.append(bicicleta) #para modificar lista, para leer solo tupla
    return lista_retorno

def csv_bicicletas_filtradas(lista:list, tipo_bici: str):
    """
    Filtra bicicletas de una lista por un tipo específico y las guarda en un archivo CSV.

    Parameters:
    lista : list of dict
        Una lista de diccionarios que contienen la información de cada bicicleta.
        Cada diccionario debe contener al menos las claves 'id_bike', 'nombre', 'tipo' y opcionalmente 'tiempo'.

    tipo_bici : str
        El tipo de bicicleta por el cual se desea filtrar y nombrar el archivo CSV.
        Debe ser uno de los siguientes valores: 'BMX', 'PLAYERA', 'MTB' o 'PASEO'.

    Returns:
    None

    Raises:
    ValueError
        Si la lista está vacía o si alguno de los diccionarios en la lista no contiene las claves requeridas.
    """
    import csv
    import os
    
    tipo_bici = tipo_bici.upper()
    bicis_filtradas = filtrar_bicicletas(lista, tipo_bici)

    if not bicis_filtradas:
        print(f"No se encontraron bicicletas del tipo '{tipo_bici}' para escribir en el archivo CSV.")
        return
    
    nombre_archivo = f'{tipo_bici}.csv'
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

    encabezados = ['id_bike', 'nombre', 'tipo', 'tiempo']

    

    with open(ruta_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=encabezados)

        writer.writeheader()
        for bicicleta in bicis_filtradas:
            writer.writerow({
                'id_bike': bicicleta['id_bike'],  # Utiliza el identificador único existente
                'nombre': bicicleta['nombre'],
                'tipo': bicicleta['tipo'],
                'tiempo': bicicleta['tiempo']  # Agregar tiempo si está presente en bicicleta
            })

    print(f"Archivo CSV '{nombre_archivo}' creado exitosamente con las bicicletas del tipo '{tipo_bici}'.")

##############################
###########PUNTO 6############
##############################

def calcular_promedio_por_tipo(lista: list):
    """
    Calcula el promedio de tiempo por cada tipo de bicicleta en una lista de bicicletas.

    Parameters:
    lista : list of dict
        Una lista de diccionarios que contienen la información de cada bicicleta.
        Cada diccionario debe contener al menos las claves 'tipo' y 'tiempo'.

    Returns:
    None

    Prints:
    Imprime por consola el promedio de tiempo para cada tipo de bicicleta presente en la lista.
    Si no hay bicicletas de algún tipo, el promedio para ese tipo será 0.00 minutos.
    """
    tipo_bici = ['BMX', 'PLAYERA', 'MTB', 'PASEO']
    promedios = {tipo: {'total_tiempo': 0, 'conteo': 0} for tipo in tipo_bici} #conteo es la cantidad de bici x tipo
    
    for bicicleta in lista:
        tipo = bicicleta['tipo']
        tiempo = bicicleta['tiempo']
        
        if tipo in promedios:
            promedios[tipo]['total_tiempo'] += tiempo
            promedios[tipo]['conteo'] += 1
    
    for tipo, datos in promedios.items():
        promedio = datos['total_tiempo'] / datos['conteo'] if datos['conteo'] > 0 else 0
        print(f"Promedio de tiempo para bicicletas tipo '{tipo}': {promedio:.2f} minutos.") 

##############################
###########PUNTO 7############
##############################

def swap_lista(lista:list, i:int, j:int)-> None:
    """
    Intercambia dos elementos en una lista dada.

    Parameters:
    lista : list
        La lista en la cual se realizará el intercambio.
    i : int
        Índice del primer elemento a intercambiar.
    j : int
        Índice del segundo elemento a intercambiar.

    Returns:
    None

    Modifica la lista 'lista' intercambiando los elementos en las posiciones 'i' y 'j'.
    """
    aux = lista[i] # en este caso seria otra lista
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_bicicletas_tipo_tiempo(bicicletas:list):
    """
    Ordena una lista de bicicletas primero por tipo y luego por tiempo ascendente.

    Parameters:
    bicicletas : list
        Lista de diccionarios donde cada diccionario representa una bicicleta con las claves 'tipo' y 'tiempo'.

    Returns:
    None

    Modifica la lista 'bicicletas' ordenándola de acuerdo al tipo de bicicleta (en orden alfabético) y, 
    dentro de cada tipo, por tiempo ascendente.
    """
    tam = len(bicicletas)
    for i in range(tam - 1):
        for j in range(i+1, tam):
            if bicicletas[i]["tipo"] == bicicletas[j]["tipo"]: #agrupo los empleados del mismo sector
                    if bicicletas[i]["tiempo"] > bicicletas[j]["tiempo"]: #dentro del genero, agrupo por orden alfabetico
                        swap_lista(bicicletas, i, j)
            elif bicicletas[i]["tipo"] > bicicletas[j]["tipo"]:
                    swap_lista(bicicletas, i, j)


##############################
###########PUNTO 8############
##############################

def guardar_en_json(lista):
    """
    Guarda una lista de bicicletas en formato JSON en un archivo llamado 'bicicletas_ordenadas.json'.

    Parameters:
    lista : list
        Lista de diccionarios donde cada diccionario representa una bicicleta.

    Returns:
    None

    Guarda la lista de bicicletas en formato JSON en el directorio actual del programa.
    Imprime un mensaje indicando la correcta ejecución de la operación.
    """
    nombre_archivo = 'bicicletas_ordenadas.json'
    directorio_actual = os.getcwd()
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(lista, file, indent = 4)
    print(f"Lista de bicicletas guardada correctamente en '{nombre_archivo}'.")
