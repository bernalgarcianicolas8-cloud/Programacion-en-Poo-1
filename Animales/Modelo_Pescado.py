from Modelo_Animal import Animal

class Animal_Pescado(Animal):
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        super().__init__(Nombre, edad, Habitad, Dieta, Tamaño, color)
    
    def Moverse(self):
        print("\nNadan con aletas y cuerpo fusiforme en agua")
          
    def comunicacion(self):
        print("\nSe comunican con feromonas y leguaje corporal")
    
    def Alimentarse(self):
        print("\nComen Placton, algas, cristaceos")
    
    def Adaptacion(self):
        print("\nSe adoptan con Branqueas y escamas en agua")
    
    def Instinto(self):
        print("\nTienen instinto de supervivencia y evitan depredadores ")
        
    def Descanso(self):
        print("\nDescansan en lugares seguros y escondidos")
    
    def Sueño(self):
        print("\nEntran en Estado de reposo y reducen su actividad")
        
    def InteraccionSocial(self):
        print("\nViven solos o en grupos y cardumenes")