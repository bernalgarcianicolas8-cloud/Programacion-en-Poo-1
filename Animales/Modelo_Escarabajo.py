from Modelo_Animal import Animal

class Animal_Escarabajo(Animal):
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        super().__init__(Nombre, edad, Habitad, Dieta, Tamaño, color)
    
    def Moverse(self):
        print("\nVuelan y caminan en 6 patas")
        
    def comunicacion(self):
        print("\nSe comunican con feromonas y sonidos")
    
    def Alimentarse(self):
        print("\nComen plantas, frutas, carroña y otros insectos")
    
    def Adaptacion(self):
        print("\nSe adaptan con exoesqueleto duro y alas")
    
    def Instinto(self):
        print("\nTienen un instinto de supervivencia y defensa")
        
    def Descanso(self):
        print("\nDescansan en lugares oscuros y seguros")
    
    def Sueño(self):
        print("\nDuermen en estado de reposo y quietud")
        
    def InteraccionSocial(self):
        print("\nviven solos o en grupos pequeños")