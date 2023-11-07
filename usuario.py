from libro import Libro

class Usuario:
    
    def __init__(self, rol):
        self.rol = rol
        self.libros_inventario = {}
        self.libros_prestados= []
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
        
        

    def hacer_prestamo(self,codigo, fecha_prestamo, inventario):
        self.prestado: True
        self.fecha_prestamo=fecha_prestamo
        self.inventario=inventario
        if codigo in self.inventario:
            self.inventario[codigo]['cantidad_disponible'] -= 1
            if self.inventario[codigo]['cantidad_disponible']==0:
                print("No hay copias disponibles de ese libro")
            else:
                self.libros_prestados.append( self.inventario[codigo])
                print("""Su préstamo fue un éxito
                      Su fecha de entrega es el: {self.fecha_prestamo}
                      """)

        
    def devolver(self, libro,inventario):
        self.prestado: False
        if libro.codigo in self.libros_inventario:
            self.inventario[libro.codigo]['cantidad_disponible'] += 1
        print('Su libro ha sido devuelto')
        
        
    def ver_libros_disponibles(self,inventario):
        self.inventario=inventario
        print("Libros disponibles en el sistema: ")
        print(self.inventario)
        
    def ver_libros_prestados(self):
        print("Historial de libros prestados: ")
        print(self.libros_prestados)
   
    