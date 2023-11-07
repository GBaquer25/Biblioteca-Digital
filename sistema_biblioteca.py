import os
from usuario import Usuario
from libro import Libro
from datetime import datetime,timedelta
class Sistema_Biblioteca:
    
    
    def __init__(self):
                self.libros_inventario = {
                    'codigo': "199",
                    'titulo': '100 años de soledad',
                    'autor': 'Garcia Marquez',
                }


    def iniciar_sesion(self):
        while True:
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            
            if usuario == "admin" and contrasena == "12345":
                usuario= Usuario("administrador")
                print("Este usuario es administrador")
            elif usuario == "est" and contrasena == "54321":
                usuario= Usuario("estudiante")
                print("Este usuario es estudiante")
            else:
                usuario= Usuario("")
                print("ingrese usuario y contraseña válidos")
            return usuario
            
            
    def menu_adm(self, usuario):
            while True:
                print("Elija la opcion que desee ejecutar")
                print("\n1) Agregar libro a inventario")
                print("2) Buscar libro")
                print("3) Regresar a iniciar sesion")
                opcion = input("Seleccione una opción (1, 2) o 'q' para salir: ")
                
                if opcion=="1":
                    print("Ingrese codigo del libro ")
                    codigo= str(input(''))
                    print("Ingrese titulo del libro ")
                    titulo= str(input(''))
                    print("Ingrese autor del libro ")
                    autor= str(input(''))
                    libro= Libro(codigo, titulo, autor)
                    usuario.agregar_libro(libro)
                
                elif opcion=="2":
                    print("Ingrese codigo del libro a buscar")
                    codigo= str(input(''))
                    usuario.buscar_libro(libro.codigo)
                    
                elif opcion=="3":
                    usuario= Usuario("")
                    self.iniciar_sesion()
                
                elif opcion.lower() == 'q':
                    break                
                else:
                    print("Elija una opcion valida") 

    def menu_estudiante(self,usuario):
            self.usuario=usuario
            while True:
                print("\n1. Ver libros disponibles")
                print("2. Ver libros prestados")
                print("3. Hacer préstamo")
                print("4) Regresar a iniciar sesion")
                opcion = input("Seleccione una opción (1,2,3,4) o 'q' para salir del programa: ")

                if opcion == '1':
                    usuario.ver_libros_disponibles(self.libros_inventario)
                elif opcion == '2':
                    usuario.ver_libros_prestados()
                elif opcion == '3':
                    codigo_libro = input("Ingrese el código del libro que desea prestar: ")
                    fecha_prestamo = datetime.now()
                    usuario.hacer_prestamo(codigo_libro, fecha_prestamo, self.libros_inventario)
                elif opcion == '4':
                    self.iniciar_sesion()
                elif opcion.lower() == 'q':
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

    def main(self):
            print("BIENVENIDO")
        
            usuario_autenticado=self.iniciar_sesion()
            if usuario_autenticado.rol=="administrador":             
                self.menu_adm(usuario_autenticado)
            elif usuario_autenticado.rol=="estudiante":
                self.menu_estudiante(usuario_autenticado)   
            else:
                print("Usuario o clave incorrecto")


   
if __name__ == "__main__":
    sistema = Sistema_Biblioteca()
    sistema.main()
      

        
        
        
        
        
        
    