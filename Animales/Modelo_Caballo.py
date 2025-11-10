from Modelo_Animal import Animal

class Animal_Caballo(Animal):
    def __init__(self, Nombre, edad, Habitad, Dieta, Tamaño, color):
        super().__init__(Nombre, edad, Habitad, Dieta, Tamaño, color)
    
    def Moverse(self):
        print("\nPuede alcanzar hasta 88km/h en galope")
    
    def comunicacion(self):
        print("\nPueden Utilizar lenguaje corporal, Vocalizaciones, Olfato, Tacto")
    
    def Alimentarse(self):
        print("\nSe alimentan de hiervas, Heno, Granos, Frutas y Verduras")
    
    def Adaptacion(self):
        print("\nSe adaptan fisica, comportamental y fisiologicamente para sobrevivir y prosperar")
    
    def Instinto(self):
        print("\nSu instinto les permite estar siempre alerta")
        
    def Descanso(self):
        print("\nEllos descansan para recuperarse fisica y mentalmente")
    
    def Sueño(self):
        print("\nDuermen de 2-4 horas")
        
    def InteraccionSocial(self):
        print("\nson animales sociales que viven en manadas, se comunican de manera no verbal y establecen jerarquias y vinculos afectivos")
