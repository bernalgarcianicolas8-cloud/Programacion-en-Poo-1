from Modelo_Animal import Animal

class Animal_Caiman(Animal):
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        super().__init__(Nombre, edad, Habitad, Dieta, Tamaño, color)
    
    def Moverse(self):
        print("\nSu movilidad es impresionante, es capaz de alcanzar velocidades de hasta 24km/h en tierra")
        print("Tambien es capaz de alcanzar ")  
          
    def comunicacion(self):
        print("\nsu comunicacion es atravez de vocalizaciones (gruñidos, Rugidos)")
    
    def Alimentarse(self):
        print("\nse alimentan de peces, crustaceos, aves y mamiferos")
    
    def Adaptacion(self):
        print("\nse adaptan facilmente al ambiente acuatico")
    
    def Instinto(self):
        print("\nTienen Instinto de caza y desfensa muy desarrollado")
        
    def Descanso(self):
        print("\nsuelen Descansar en la orilla del agua o en lugares sombreados")
    
    def Sueño(self):
        print("\nDuermen con un ojo abierto, lo que les permite estar alertar a sus depredadores")
        
    def InteraccionSocial(self):
        print("\nEs un animal solitario")