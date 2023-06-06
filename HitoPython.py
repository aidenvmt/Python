from getpass import getpass

from os import system
import os


# Variables globales que usara el programa

datos = {'Pepe':'1234', 'Juan':'4321'} #Usuarios logueados ya en el sistema

carrito = {} #Carrito vacio donde se iran añadiendo los productos

totalCarrito = sum(carrito.values()) #suma de los valores del carrito


#Declaramos todas las clases

class Producto():
    def __init__ (self,nombre,precio):
        self.nombre =nombre
        self.precio = precio
          
    def obtener_unidades(self):

        self.unidades = input("Escribe las unidades que desee: ")
 
class Factura:

    @staticmethod
    def factura():
        cliente = input("Cliente Internacional(Formato Si/No)?: ")

        match cliente.lower():
            case "si":
                try:
                    os.system("cls")
                    nombre = input("Escribe su nombre: ")
                    apellidos = input("Escribe su apellido: ")
                    direccion = input("Escribe su direccion: ")
                    ciudad = input("Escribe su ciudad: ")
                    cp = int(input("Escribe su codigo postal: "))
                        
                except:
                    print ("Error de input")
                    cliente()

                os.system("cls")
                print("------------Factura------------")
                print(f"Nombre:{nombre}  Apellidos:{apellidos} ")
                print(f"Direccion: {direccion} ")
                print(f"Ciudad: {ciudad}   CP: {cp}")
                for k,v in carrito.items():
                    print (f"Producto: {k}               Precio: {v}€")
                print (f"Precio del carrito: {round(sum(carrito.values())*1.21,2)}€")
                print ("------------------------------")
                os.system("pause")
                print("Enviando SMS...")
            case "no":
                os.system("cls")
                try:
                    os.system("cls")
                    nombre = input("Escribe su nombre: ")
                    apellidos = input("Escribe su apellido: ")
                    direccion = input("Escribe su direccion: ")
                    ciudad = input("Escribe su ciudad: ")
                    try:
                        cp = int(input("Escribe su codigo postal: "))
                    except:
                        ("error de input")
                        cp = int(input("Escribe su codigo postal: "))
                except:
                    print("Error de input")

                os.system("cls")
                print("------------Factura------------")
                print(f"Nombre:{nombre}")
                print(f"Apellidos:{apellidos} ")
                print(f"Direccion: {direccion} ")
                print(f"Ciudad: {ciudad}   CP: {cp}")
                for k,v in carrito.items():
                    print (f"Producto: {k}               Precio: {v}€")
                print (f"Precio del carrito: {round(sum(carrito.values())*1.11,2)}€")
                print ("------------------------------")
                os.system("pause")
                print("Enviando SMS...")
            case _: 
                print("Error")
                cliente = input("Cliente Internacional(Formato Si/No)?: ")



#La clase Persona Hereda de Factura ya que cada factura estara asociada a un cliente  

class Persona(Factura): #Esta clase se usara para el inicio de sesion
        
    def __init__ (self):
        self.nombre = None
        self.contraseña = None
    
    def obtener_datos(self):
        self.usuario = input("Escribe un nombre de usuario: ")
        self.contraseña = getpass("Escribe una contraseña: ")
    
        datos[self.usuario] = self.contraseña
   
    @staticmethod
    def iniciar_sesion():
        if datos:
            nombre = input ("Indique su nombre: ")
            password = input ("Indique su contraseña: ")
            for k,v in datos.items():
                if k == nombre and v == password:
                    print("Logueado")
                    a = True
                    break
                else:
                    a = False
                    
            if a == True:
                pass
            elif a == False:
                print("No esta registrado")
                exit()
            else:
                print("Error")
            
        else:
            print("No hay usuarios")
    
p1 = Persona()

def menu ():
    print ("------Hito1-------")
    print ("1. Registrarse")
    print ("2. Inicio de sesion")
    print ("------------------")

    try:    
        seleccion =input("Escriba una opcion: ")
        match seleccion:
           case "1":
               os.system("cls")
               p1.obtener_datos()

           case "2":
               os.system("cls")
               p1.iniciar_sesion()

           case _:
                print("Error de input")
                os.system("pause")
                os.system("cls")
                menu()
    except:
        print("Error")

menu()                         

camisa = Producto("Camisa",5.99)
pantalones = Producto("Pantalones",10.99)
sombrero = Producto("Sombrero",3.99)
gafas = Producto("Gafas",3.99)
chaleco = Producto("Chaleco",11.99)

#print ("Selecciona sus productos: ")

def menuProductos():

    print ("1. Camisa")
    print ("2. Pantalones")
    print ("3. Sombrero")
    print ("4. Gafas")
    print ("5. Chaleco")
    print("-----------------------------")
    print ("0. Borrar objetos del carrito")
    
    seleccion_productos =input("Seleccione sus productos: ")
    match seleccion_productos:
        case "1" :
            print (f"{camisa.nombre}   {camisa.precio}€")
            print("Presiona 0 para volver")
            carrito[camisa.nombre] = camisa.precio
            try:
                camisa.unidades = input("Escribe las unidades que desee: ")
                precioTotal = camisa.precio * int(camisa.unidades)
                carrito[camisa.nombre] = precioTotal
                print (f"El precio del carrito es: {precioTotal}€")
            except:
                print("Error de input")
                os.system("pause")
                os.system("cls")
                menuProductos()
            
        case "2":
            print (f"{pantalones.nombre}    {pantalones.precio}€")
            print("Presiona 0 para volver")
            carrito[pantalones.nombre] = pantalones.precio
            try:
                pantalones.unidades = int(input("Escribe las unidades que desee: "))
                precioTotal = pantalones.precio * int(pantalones.unidades)
                carrito[pantalones.nombre] = precioTotal
                print (f"El precio del carrito es: {precioTotal}€")
            
            except:
                print("Error")
                os.system("pause")
                os.system("cls")
                menuProductos()
                          
        case "3":
            print (f"{sombrero.nombre}    {sombrero.precio}€")
            print("Presiona 0 para volver")
            carrito[sombrero.nombre] = sombrero.precio 
            try:
                sombrero.unidades = input("Escribe las unidades que desee: ")
                precioTotal = sombrero.precio * int(sombrero.unidades)
                carrito[sombrero.nombre] = precioTotal
                print (f"El precio del carrito es: {precioTotal}€")
            except:
                print("Error de input")
                os.system("pause")
                os.system("cls")
                menuProductos()
           
        case "4":
            print (f"{gafas.nombre}    {gafas.precio}€")
            print("Presiona 0 para volver")
            carrito[gafas.nombre] = gafas.precio 
            try:
                gafas.unidades = input("Escribe las unidades que desee: ")
                precioTotal = gafas.precio * int(gafas.unidades)
                carrito[gafas.nombre] = precioTotal
                print (f"El precio del carrito es: {precioTotal}€")
            except:
                print("Error de input")
                os.system("pause")
                os.system("cls")
                menuProductos()
            
        case "5":
            print (f"{chaleco.nombre}    {chaleco.precio}€")
            print("Presiona 0 para volver")
            carrito[chaleco.nombre] = chaleco.precio
            try:
                chaleco.unidades = input("Escribe las unidades que desee: ")
                precioTotal = chaleco.precio * int(chaleco.unidades)
                carrito[chaleco.nombre] = precioTotal
                print (f"El precio del carrito es: {precioTotal}€")
            except:
                print("Error de input")
                os.system("pause")
                os.system("cls")
                menuProductos()
            
        case "0":
            try:
                print(carrito)
                borrar_items = input("Escribe que objeto quieres borrar: ") 
                del(carrito[borrar_items])
                print(carrito)
            except:
                pass
        case _:
            print("No existe el producto")

menuProductos()

def selecciones():

    try:
        seleccionar_productos_denuevo = input("Deseas escoger otro producto (Formato Si/No)?: ")   

        while  True:
            if seleccionar_productos_denuevo.lower() == "si":
                menuProductos()
                seleccionar_productos_denuevo = input("Deseas escoger otro producto (Formato Si/No)?: ")
            if seleccionar_productos_denuevo.lower() == "no":
                break
            else:
                print("Error de input")
                selecciones()
                break

    except:
        pass

selecciones()

p1.factura()
