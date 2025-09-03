"""

Crea un archivo llamado sistema_inventario.py donde implementarás todo el código del sistema.

Define la clase Producto con un método constructor que inicialice los atributos nombre (str), precio (float) y cantidad (int). Incluye validaciones para que el precio no sea negativo, el nombre no esté vacío y la cantidad sea mayor o igual a cero.

Añade a la clase Producto los siguientes métodos:

actualizar_precio(nuevo_precio): para modificar el precio validando que sea positivo
actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea positiva
calcular_valor_total(): que devuelva el valor total (precio × cantidad)
__str__(): para mostrar la información del producto de forma legible
Crea la clase Inventario con un constructor que inicialice una lista vacía para almacenar productos.

Implementa en la clase Inventario los siguientes métodos:

agregar_producto(producto): para añadir un objeto de tipo Producto a la lista
buscar_producto(nombre): para encontrar un producto por su nombre
calcular_valor_inventario(): para sumar el valor total de todos los productos
listar_productos(): para mostrar todos los productos del inventario
Implementa un manejo de excepciones utilizando bloques try-except para capturar errores como valores negativos, tipos de datos incorrectos o productos no encontrados.


Método constructor que inicialice los atributos:
    - nombre (str)
    - precio (float)
    - cantidad (int).
    
    Incluye validaciones para:
    - el precio no sea negativo
    - el nombre no esté vacío
    - la cantidad sea mayor o igual a cero.

Crea una función menu_principal() que muestre opciones al usuario (1. Agregar producto, 2. Buscar producto, etc.) y procese la entrada del usuario.

En la sección principal del programa (bajo if __name__ == "__main__":), instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.

"""


# Importación de módulos

import os # Importamos para limpiar consola al mostrar distintas opciones al usuario
import re # Usamos regex para validar
import json # Usado para validar el contenido de las instancias de clase, somentar al finalizar



# Funciones

def clear():
    # Varía: para Windows es 'cls', en sistemas Mac es 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


class Producto:

    """ Clase que encapsula la información de un producto """

    def __init__(self, nombre:str, precio:float, cantidad:int):

        """
        Constructor de la clase Producto

        nombre -- nombre del producto
        precio -- precio del producto (número positivo con decimales)
        cantidad -- entero > 0
        
        """

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self,nuevo_precio):
        
        self.precio = nuevo_precio

    def actualizar_cantidad(self,nueva_cantidad):
        
        self.cantidad = nueva_cantidad

    def __str__(self):
        
        return f"El producto {self.nombre} tiene un precio de {self.precio:.2f}€ y hay {self.cantidad} productos en stock"


class Inventario:

    """ Clase que genera un inventario, almacena productos y da información del mismo """

    def __init__(self):
        self.productos = {} # Generamos una diccionario en la que almacenar productos, usamos cono id el nombre del producto
    
    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        return self.productos.get(nombre)
    
    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)

def menu_principal():

    menu = {
        "PRODUCTOS": [
            "1.- Añadir un nuevo producto",
            "2.- Modificar el precio de un producto",
            "3.- Modificar la cantidad de un producto"
        ],
        "INVENTARIO": [
            "4.- Buscar un producto del inventario por su nombre",
            "5.- Listar todos los productos del inventario"
        ]           
    }

    print("** MENÚ PRINCIPAL ** \nPulsa el número de la acción que quieras realizar\n\n")

    num_opciones = 0
    for categoria, opciones in menu.items():
            
            print(f"== {categoria} ==")
            for opcion in opciones:
                print(opcion)
                num_opciones += 1
            print()



    # Realizamos la petición y validación de que se introduce un valor correcto
    while True:
        
        accion_menu = input("Introduce el número de la acción (de 1 a " + str(num_opciones)  + "): ")

        if accion_menu.isdigit() and 1 <= int(accion_menu) <= num_opciones:
        
            break
        
        else:
            print("La opción no es válida, introduce un número de acción del 1 ala", str(num_opciones))

    return(accion_menu)


def volver_menu(error=None):

    if error != None:

        print(error)

    
        while True:
            volver = input("Pulsa Enter para volver al menú")
            if volver == "":   # Solo Enter
                clear()
                break

    return None


def buscar_producto_input():

    clear()

    while True:

        # Nombre no se valida
        nombre = input("Introduce el nombre del producto: ")
        busqueda = inventario.buscar_producto(nombre)


        if busqueda is None:
           
            volver_menu("Producto no encontrado con ese nombre")
            break

        else:

            break

    return(busqueda)

def validar_precio():
    
        # Precio se valida un número positivo con 2 decimales
    while True:

        precio = input("Introduce el precio del producto (número positivo, con dos decimales separados por , -> 15,95): ").replace(",",".")

        # validación de formato: al menos un dígito, punto, y exactamente 2 decimales
        if precio.count(".") == 1 and len(precio.split(".")[1]) == 2 and precio.replace(".", "").isdigit():
            
            precio = float(precio)
            
            if precio > 0:

                break

            else:

                print("El precio debe ser mayor que 0.")
            
        else:
            
            print("Eso no es un número positivo con dos decimales, inténtalo de nuevo.")   

    return(precio)


def validar_cantidad():

    # Cantidad se valida un entero positivo
    while True:
    
        try: 

            cantidad = int(input("Introduce la cantidad de stock (número entero positivo): ").strip())
        
            if cantidad > 0:
                
                break

        except ValueError:

            print('Recuerda que has de introducir un número entero')  

    return(cantidad)

def validar_nombre(new=False):

    # Cantidad se valida un entero positivo
    while True:
    
        nombre = input("Introduce el nombre del producto: ").lower()
    
        if inventario.buscar_producto(nombre) is None and new is True:
            
            break

        elif new is True: 

            volver_menu("Ya existe un producto con ese nombre.")

        else:

            break


    return(nombre)
    

def agregar_producto_input():

    clear()

    # Realizamos la petición y validación de que se introduce un valor correcto

    nombre = validar_nombre(True)

    precio = validar_precio()

    cantidad = validar_cantidad()

    # Con todos los datos correctos, creamos producto y lo guardamos en inventario
    print("PRODUCTO A CREAR:", nombre, precio, cantidad)
    return Producto(nombre, precio, cantidad)



def actualizar_precio_input(producto):

    
    print("Vas a modificar el precio del siguiente producto")
    print(producto)

    precio = validar_precio()

    return precio




# Inicializamos el inventario
inventario = Inventario()

def main():
    

    # Sólo para validación del inventario
    def validar_inventario():

        
        print("Listado de productos")
        # Sólo para validar
        

        print(json.dumps(inventario.__dict__, indent=2, ensure_ascii=False,
                        default=lambda o: o.__dict__))         




    # Imprimimos el menú principal y recogemos la opción elegida

    while True: # Bucle del menú principal

        opcion = menu_principal()


        # 1.- Añadir un nuevo producto        
        if opcion == "1":
        
            producto = agregar_producto_input()
            inventario.agregar_producto(producto)

            # Sólo para validar, comentar en producción
            #validar_inventario()

        
        # 2.- Modificar el precio de un producto        
        elif opcion == "2":

            if len(inventario.productos) > 0:
            
                producto = buscar_producto_input()


                if producto is None:
                    continue

                precio = actualizar_precio_input(producto)


                if precio is None:
                    continue


                producto.actualizar_precio(precio)
                volver_menu("Precio actualizado")


            else:

                volver_menu("Todavía no has dado de alta ningún producto")

        # 3.- Modificar la cantidad de un producto        
        elif opcion == "3":

            if len(inventario.productos) > 0:
            
                producto = buscar_producto_input()

                if producto is None:
                    continue
                cantidad = validar_cantidad()

                if cantidad is None:
                    continue

                producto.actualizar_cantidad(cantidad)
                volver_menu("Cantidad actualizada")

            else:

                volver_menu("Todavía no has dado de alta ningún producto")

        # 4.- Buscar un producto del inventario por su nombre
        elif opcion == "4":

            if len(inventario.productos) > 0:
            
                producto = buscar_producto_input()

                if producto is None:
                    continue

                print(producto)
                volver_menu()                
                
            else:

                volver_menu("Todavía no has dado de alta ningún producto")                

        # 5.- Listar todos los productos del inventario

        else:

            if len(inventario.productos) > 0:

                inventario.listar_productos()
                volver_menu()

            else: 

                volver_menu("No existen productos en el inventario")

            
    

# Ejecución de main si se "EJECUTA el programa" directamente
# En caso contrario ("import") se hacen disponibles las funciones sin ejecución directa
if __name__ == "__main__":
    main()