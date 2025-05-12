# Validador y Gestor de Correos Electrónicos para Biblioteca Universitaria
import re

# la siguiente funcion muestra el menú de opciones
def menu():
        while True:
            print('Menu Principal:\n\n'
                  '1. Registrar un nuevo correo electrónico.\n'
                  '2. Ver correos registrados.\n'
                  '3. Buscar correos registrados.\n'
                  '4. Salir.\n')
            opcion = int(input('Seleccione una opcion: '))
            if opcion == 1:                                                 #Registra el correo ingresado
                correo=str(input('Escriba un Correo: ')).lower().strip()    #El correo ingresado lo convierte en minusculas y recorta los espacios al principio y final de la cadena de caracteres
                validarCorreo(correo)                                       #Valida el correo, lo clasifica y lo añade a la lista de correos
                clasificarCorreo(correo)
                agregarCorreo(correo)
                print("Felicidades! el correo", correo, "fue añadido con exito")
            elif opcion == 2:                                               #Muestra la lista de correos registrados
                print('Correos registrados:\n', lista_correos)
            elif opcion == 3:                                               #Busca y devuelve coincidencias de los correos registrados
                buscarCorreo(lista_correos)
            elif opcion == 4:                                               #Finaliza el programa
                exit()



lista_correos=[]
#la siguiente funcion añade los correos recibidos
def agregarCorreo(correo):
    lista_correos.append(correo)
    return True

#La siguiente funcion valida si el correo ingresado cumple con el formato solicitado y lo devuelve, en caso de que no,
#imprime un error y vuelve a ejecutar la funcion para mostrar el menú
def validarCorreo(correo):
    resultado = re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[A-Za-z]{2,}(?:\.[a-z]{2,})*$', correo)
    if resultado is not None:
        return True, correo
    elif resultado is None:
        print('Formato de Correo invalido'), menu()
    return False

#se crea una lista para los estudiantes y otra para los profesores, a los cuales se añadiran los correos escritos
estudiante=[]
profesor=[]
#Se clasifican los correos en profesores y estudiantes de acuerdo al formato en el que terminan
def clasificarCorreo(correo):
    #Si el correo ingresado termina en el patrón mostrado, lo añade a la lista estudiantes o profesor segun dependa
    #Si el correo ingresado no coincide con ninguno de los 2 formatos anteriores, muestra un error y ejecuta el menú nuevamente
    if correo.endswith("@estudiante.utv.edu.co"):
        estudiante.append(correo)
        return print(estudiante)
    elif correo.endswith("@utv.edu.co"):
        profesor.append(correo)
        return print(profesor)
    else:
        return print("Correo invalido, escriba un correo valido"), menu()

#Esta función se encarga de buscar en la lista de correos las coincidencias de las palabras que la persona escriba
#Devuelve el o los correos que coincidan con la palbra escrita en una lista
def buscarCorreo(correo_buscado):
    correo_buscado=input("Ingrese el correo a buscar: ")
    filtro = filter(lambda elemento: correo_buscado in elemento, lista_correos)
    filtro = list(filtro)
    if len(filtro) == 0:
        return print("el correo buscado no existe o no ha registrado correos"), menu()
    else:
        return print("la palabra buscada coincide con el siguiente o siguientes correos:", filtro)

#Este comando inicia el programa
menu()
