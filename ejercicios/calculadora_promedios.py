# Importación de módulos

import numpy as np # Módulo para cálculo de estadísticos (se podría usar para eso cálculo nativo pero pruebo con numpy)

# DEFINICIÓN DE VARIABLES GLOBALES
# Variables que queremos disponibles para el total de las funciones

import variables

calificaciones = []
asignaturas = []
alumno = {
    "calificaciones": {},
    "promedio": None,
    "aprobadas": [],
    "suspensas": [],
    "maxima_calificacion": {},
    "minima_calificacion": {},
}

# DECLARACIÓN DE FUNCIONES AUXILIARES
# Reutilización y organización de código

def ingresar_calificaciones():
    
    """
    Función que solicita al usuario asignaturas y calificaciones,
    almacenándolas en las listas correspondientes

    Argumentos:
    - Sin argumentos

    REQUERIMIENTOS

    Solicitar al usuario que ingrese el nombre de la materia
    Solicitar la calificación (validando que sea un número entre 0 y 10)
    Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
    Preguntar si desea continuar ingresando más materias
    Retornar ambas listas cuando el usuario decida terminar


    """

    while True:

        # Solicitamos la asignatura (no se valida el nombre)
        asignatura = input("Introduce el nombre de la asignatura: ")

        # Solicitamos la calificación (se valida un número de 0 a 10)
        while True:

            calificacion = input("Introduce la calificación (de 0 a 10, máximo 2 decimales separados por coma): ").strip().replace(",",".")

            try: 

                # Redondeamos a 2 decimales por si se han introducido más (no se valida espefícicamente)
                calificacion = round(float(calificacion),2)
                
                if 0 <= calificacion <= 10:
                    
                    break

                else:

                    print('Las calificacion válidas van entre 0 y 10')                    

            except ValueError:

                print('Formato de datos no válido. Recuerda: Números del 1 al 10 con dos decimales máximo separados por ,')                    


        # Añadimos a las listas correspondientes la asignatura y calificación
        
        asignaturas.append(asignatura)
        calificaciones.append(calificacion)

        
        # Control de estado de listas
        #print(asignaturas)
        #print(calificaciones)
        
        
        # Preguntamos si se desean introducir más calificaciones

        continuar = input("Introduce SI para continuar introduciendo asignaturas: ").strip().lower()

        # Si no se contesta si, rompemos el bucle
        if continuar != "si":
        
            break


    # Impresión de salida, lista de asignaturas y calirifaciones introducidas

    print("Estas son las calificaciones introducidas:")
   
    # Recorro los datos introducidos y los visualizo
    for i in range(0, len(asignaturas)):
        print(asignaturas[i], ":", calificaciones[i])


    return


def calcular_promedio(calificaciones):

    """
    Función que calcula el promedio de las clasificaciones del usuario.

    Argumentos:
    - Clasificaciones: lista de clasificaciones (notas de 1 a 10) de las distintas asignaturas del usuario


    """

    calificaciones = np.array(calificaciones)
    alumno["promedio"] = float(np.mean(calificaciones)) # Tenemos que añadir float para que no nos almacene el objeto np completo



    return


def determinar_estado(calificaciones, umbral):

    """
    Función que calcula las asignaturas aprobadas y suspensas en base a las calificaciones obtenidas y el umbral asignado (por defecto 5.0).

    Argumentos:
    - Clasificaciones: lista de clasificaciones (notas de 1 a 10) de las distintas asignaturas del usuario
    - Umbral: Umbral que define la nota que separa aprobado y suspenso (por defecto 5.0)


    """     

    for asignatura, nota in calificaciones.items():

        if nota >= umbral:
            
            alumno["aprobadas"].append(asignatura)

        else:

            alumno["suspensas"].append(asignatura)

    return


def encontrar_extremos(calificaciones):


    """
    Función que calcula las asignaturas con la nota máxima y mínima de entre las clasificaciones asignadas.

    Argumentos:
    - Clasificaciones: lista de clasificaciones (notas de 1 a 10) de las distintas asignaturas del usuario
    - Umbral: Umbral que define la nota que separa aprobado y suspenso (por defecto 5.0)


    """    

    maximo = max(calificaciones.values()) # Nos devuelve el valor máximo
    minimo = min(calificaciones.values()) # Nos devuelve el valor mínimo

    # Con la nota ya podemos tener las asignaturas de los extremos (podemos tener varias asignaturas con notras máximas o mínimas - misma nota)

    alumno["maxima_calificacion"]["asignaturas"] = [asignatura for asignatura, calificacion in calificaciones.items() if calificacion == maximo]
    alumno["maxima_calificacion"]["calificacion"] = float(maximo)


    alumno["minima_calificacion"]["asignaturas"] = [asignatura for asignatura, calificacion in calificaciones.items() if calificacion == minimo]
    alumno["minima_calificacion"]["calificacion"] = float(minimo)


    return

# FUNCIÓN PRINCIPAL

def main():


    # LÓGICA PRINCIPAL

    # 1.- Solicitamos las calificaciones del usuario
    ingresar_calificaciones()

    # 2.- Convertimos listas en la actualización de datos sobre la variable final del alumno
    for i in range(len(asignaturas)):
        alumno["calificaciones"][asignaturas[i]] = calificaciones[i]

    
    # 3.- Calculamos el promedio enviando únicamente las calificaciones
    calcular_promedio(list(alumno["calificaciones"].values()))

    # 4.- Calculamos el estado de las asignaturas
    determinar_estado(alumno["calificaciones"],variables.umbral_calculadora)

    # 5.- Calculamos las notas máximas y mínimas
    encontrar_extremos(alumno["calificaciones"])

    # 6.- IMPRIMIMOS EL REPORTE FINAL

    print("El promedio de tus calificaciones es:" , round(alumno["promedio"],2))

    print("Has aprobado las siguientes asignaturas:", ", ".join(str(x) for x in alumno["aprobadas"]))

    print("Has suspendido las siguientes asignaturas:", ", ".join(str(x) for x in alumno["suspensas"]))

    print("Tu nota máxima las has obtenido en:", ", ".join(str(x) for x in alumno["maxima_calificacion"]["asignaturas"]), "con una nota de", alumno["maxima_calificacion"]["calificacion"])

    print("Tu nota mínima las has obtenido en:", ", ".join(str(x) for x in alumno["minima_calificacion"]["asignaturas"]), "con una nota de", alumno["minima_calificacion"]["calificacion"])


# Ejecución de main si se "EJECUTA el programa" directamente
# En caso contrario ("import") se hacen disponibles las funciones sin ejecución directa
if __name__ == "__main__":
    main()