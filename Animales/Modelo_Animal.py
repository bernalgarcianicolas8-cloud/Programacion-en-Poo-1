class Animal:
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        self.Nombre = Nombre
        self.edad = edad
        self.Habitad = Habitad
        self.Dieta = Dieta
        self.Tamaño = Tamaño
        self.color = color
    
    def ImprimirDatos(self):
        print(f"\nNombre: {self.Nombre}")
        print(f"\nEdad: {self.edad}")
        print(f"\nHabitad: {self.Habitad}")
        print(f"\nDieta: {self.Dieta}")
        print(f"\nTamaño: {self.Tamaño}")
        print(f"\nColor: {self.color}")

