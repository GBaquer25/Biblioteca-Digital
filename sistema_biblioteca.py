import os
from usuario import Usuario
from libro import Libro

class Sistema_Biblioteca:
    
    
        def __init__(self):
                self.libros_inventario = {}


def iniciar_sesion():
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if usuario == "admin" and contrasena == "12345":
            usuario= Usuario("administrador")
            print("Este usuario es administrador")
        elif usuario == "est" and contrasena == "54321":
            usuario= Usuario("estudiante")
            print("Este usuario es estudiante")
        return usuario
    
      


def main():
        print("BIENVENIDO")
        
        usuario_autenticado=iniciar_sesion()
        if usuario_autenticado.rol=="administrador":             usuario_autenticado.menu_adm()
        elif usuario_autenticado.rol=="estudiante":
             usuario_autenticado.menu_estudiante()   
        else:
            print("Usuario o clave incorrecto")

        
            
        
        
        
        
        
   
if __name__ == "__main__":
    main()

        
        
        
        
        
        
    