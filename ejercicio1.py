'''
### 2.1. Creación de la clase **Libro**.
###  Explicación del ejercicio:

En este ejercicio, definiremos una clase llamada `Libro` que representa un libro en nuestro futuro e-commerce.
### 2.2. Métodos adicionales para la clase **Libro**.
###  Explicación del ejercicio:

En este ejercicio, ampliaremos la clase `Libro` con métodos adicionales para establecer la cantidad de 
libros disponibles y obtener información detallada del libro.
'''

class Libro:
    def __init__(self, titulo, autor, precio) -> None:
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.cantidad= 0 
    
    def establecer_cantidad(self):
        while True:
            try:
                cantidad = int(input(f'Introduzca la cantidad de libros de: {self.titulo}'))
                if cantidad <0:
                    print('No puede haber una cantidad negativa de libros')
                else: 
                    self.cantidad = cantidad
                    break
            except ValueError:
                print('Introduce un número válido')
    
        
        
libro1 = Libro(titulo ="La Comunidad del Anillo", autor = "J.R.R.Tolkien" , precio=29.99)

libro1.establecer_cantidad()
