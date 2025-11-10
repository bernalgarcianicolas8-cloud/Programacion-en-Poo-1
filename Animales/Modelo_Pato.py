from Modelo_Animal import Animal

class Animal_pato(Animal):
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        super().__init__(Nombre, edad, Habitad, Dieta, Tamaño, color)
        
    def Moverse(self):
        print("\nVuelan caminan y nadan con patas palmeadas")
        
    def comunicacion(self):
        print("\nSe comunican con graznidos y lenguaje Corporal")
    
    def Alimentarse(self):
        print("\ncomen plantas acuaticas, insectos y pequeños cristaceos")
    
    def Adaptacion(self):
        print("\nSe adaptan con plumas, pico ancho y patas palmeadas")
    
    def Instinto(self):
        print("\nTienen un instinto de migracion y cuidado de crias")
        
    def Descanso(self):
        print("\ndescansan en agua o en nidos seguros")
    
    def Sueño(self):
        print("\nduermen con un ojo abierto y alerta")
        
    def InteraccionSocial(self):
        print("\nViven en grupos y forma parejas monogamas")