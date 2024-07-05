from funciones import *

is_running = True
csv_cargado = False
tiempos_asignados = False

while is_running == True:
    cartel_menu()
    opciones = opciones_menu('Cargar archivo .CSV', 'Imprimir lista', 'Asignar tiempos', 'Informar ganador', 'Filtrar por tipo', 'Informar promedio por tipo', 'Mostrar posiciones', 'Guardar posiciones', 'Salir')
    print(opciones)

    opcion = input('Selecciona la opción deseada (1-9): ')
    while opcion not in ['1','2','3','4','5','6','7','8','9']:
        opcion = input('Opción no válida. Selecciona la opción deseada (1-9): ')


    match opcion:
        case '1':
            lista_de_bicicletas = cargar_csv()
            csv_cargado = True
        case '2':
            if csv_cargado:
               imprimir_lista_de_bicicletas(lista_de_bicicletas)
            else:
                print('Antes de imprimir una lista, carga el archivo que deseas procesar.')
        case '3':
            if csv_cargado == True:
                lista_tiempo = mapear_lista_asignar_tiempo(lista_de_bicicletas)
                imprimir_lista_de_bicicletas(lista_de_bicicletas)
                tiempos_asignados = True
            else:
                print('El archivo .CSV no fue cargado, no hay elemento al cual asignarle tiempos.')
        case '4':
            if tiempos_asignados == True and csv_cargado == True:
                ganadores = informar_ganador(lista_de_bicicletas)
            else:
                print('No podemos informar un ganador, primero carga la información de tiempos y/o carga el archivo .CSV')
        case '5':
            if csv_cargado == True:
                tipo_de_bicicleta = pedir_tipo_de_bicicleta_filtrar()
                filtro_bicicletas = filtrar_bicicletas(lista_de_bicicletas, tipo_de_bicicleta)
                csv_bicicletas_filtradas(lista_de_bicicletas,tipo_de_bicicleta)
            else:
                print('No hay información para filtrar. Carga el archivo .CSV')
        case '6':
            if tiempos_asignados == True and csv_cargado == True:
                promedio_por_tipo = calcular_promedio_por_tipo(lista_de_bicicletas)
            else:
                print('Antes de informar los promedios de tiempo debes asegurarte de asignar los tiempos y/o cargar el archivo .CSV')
        case '7':
            if tiempos_asignados == True and csv_cargado == True:
                ordenar_bicicletas_tipo_tiempo(lista_de_bicicletas)
                imprimir_lista_de_bicicletas(lista_de_bicicletas)
            else:
                print('Antes de mostrar las posiciones debes asegurarte de asignar los tiempos y/o cargar el archivo .CSV')
        case '8':
            if csv_cargado == True:
                guardar_en_json(lista_de_bicicletas)
            else:
                print('No hay información para guardar en el JSON')
        case '9':
            print('GRACIAS POR UTILIZAR MI PROGRAMA DE PROCESAMIENTO DE DATOS.')
            is_running = False