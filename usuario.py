from libro import Libro
class Usuario:
    
    def __init__(self, rol):
        self.rol = rol
        self.libros_inventario = {}
        #self.sistema=sistema
        
    
#Metodos para administrador
    def agregar_libro(self, libro):
        if libro.codigo in self.libros_inventario:
            self.libros_inventario[libro.codigo]['cantidad_disponible']+=1
        else:
            self.libros_inventario[libro.codigo] = {
                'titulo': libro.titulo,
                'autor': libro.autor,
                'cantidad_disponible': 1
            }
        print(f"Nuevo libro agregado al sistema: {libro.titulo}")
        
        
    def buscar_libro(self,codigo):
        if codigo in self.libros_inventario:
            print(self.libros_inventario[codigo])
            return self.libros_inventario[codigo]
        else:
            return "Libro no existe en el sistema"
        
    def menu_adm(self):
        
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
                self.agregar_libro(libro)
            
            elif opcion=="2":
                print("Ingrese codigo del libro a buscar")
                codigo= str(input(''))
                self.buscar_libro(libro.codigo)
            
            elif opcion.lower() == 'q':
                break                
            else:
                print("Elija una opcion valida")
        
    
    #Metodos para estudiante
    
    def menu_estudiante(self):
        while True:
            print("\n1. Ver libros disponibles")
            print("2. Ver libros prestados")
            print("3. Hacer préstamo")
            print("4) Regresar a iniciar sesion")
            opcion = input("Seleccione una opción (1,2,3,4) o 'q' para salir del programa: ")

            if opcion == '1':
                self.ver_libros_disponibles()
            elif opcion == '2':
                self.ver_libros_prestados()
            elif opcion == '3':
                codigo_libro = input("Ingrese el código del libro que desea prestar: ")
                fecha_prestamo = input("Ingrese la fecha de préstamo: ")
                fecha_devolucion = input("Ingrese la fecha de devolución: ")
                self.hacer_prestamo(codigo_libro, fecha_prestamo, fecha_devolucion)
            #elif opcion == '4':
            #    self.ver_libros_prestados()
            elif opcion.lower() == 'q':
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    
    def prestar(self,libro):
        self.prestado: True
        if libro.codigo in self.libros_inventario:
            self.libros_inventario[libro.codigo]['cantidad_disponible'] -= 1
            #if libros_inventario[libro.codigo]['cantidad_disponible']==0:
                #print("No hay copias disponibles de ese libro")
        print('Su préstamo fue un éxito')

        
    def devolver(self, libro):
        self.prestado: False
        if libro.codigo in self.libros_inventario:
            self.libros_inventario[libro.codigo]['cantidad_disponible'] += 1
        print('Su libro ha sido devuelto')
        
        
    def ver_libros_disponibles(self):
        print("Libros disponibles en el sistema: ")
        print(self.libros_inventario)
        
       
   
    