from Modelo_Caballo import Animal_Caballo
from Modelo_Caiman import Animal_Caiman
from Modelo_Pescado import Animal_Pescado
from Modelo_Escarabajo import Animal_Escarabajo
from Modelo_Pato import Animal_pato

while True:
    print("1. Caballo")
    print("2. Caiman")
    print("3. Pescado")
    print("4. Escarabajo")
    print("5. Pato")
    print("6. salir del menu")
    opcion = int(input("Ingrese la Opcion que desee consultar: "))
    match opcion:
        case 1:
            caballo = Animal_Caballo("Caballo", "25-30 años", "Sabanas y Praderas", "Hojas, Granos, Hiervas", "1.60m Altura", "Negro, Marron y Blanco" ) 
            caballo.ImprimirDatos()
            caballo.Moverse()
            caballo.comunicacion()
            caballo.Alimentarse()
            caballo.Adaptacion()
            caballo.Instinto()
            caballo.Descanso()
            caballo.Sueño()
            caballo.InteraccionSocial()
        case 2: 
            caiman = Animal_Caiman("Caiman", "30-40 años", "Acuatico", "Peces, crustaceos, aves", "2.5m a 4m", "Verde oscuro o grisaceo, blanco o crema")
            caiman.ImprimirDatos()
            caiman.Moverse()
            caiman.comunicacion()
            caiman.Alimentarse()
            caiman.Adaptacion()
            caiman.Instinto()
            caiman.Descanso()
            caiman.Sueño()
            caiman.InteraccionSocial()
        case 3: 
            pescado = Animal_Pescado("Pescado", "5-10 años", "Acuatico", "Placton, algas, insectos", "10-50Ccm", "Variedad de colores")
            pescado.ImprimirDatos()
            pescado.Moverse()
            pescado.comunicacion()
            pescado.Alimentarse()
            pescado.Instinto()
            pescado.Descanso()
            pescado.Sueño()
            pescado.InteraccionSocial()
        case 4: 
            Escarabajo = Animal_Escarabajo("escarabajo", "unos meses", "terrestre", "plantas, hongos, insectos", "1-50 mm", "Variedad de colores")
            Escarabajo.ImprimirDatos()
            Escarabajo.Moverse()
            Escarabajo.comunicacion()
            Escarabajo.Alimentarse()
            Escarabajo.Instinto()
            Escarabajo.Descanso()
            Escarabajo.Sueño()
            Escarabajo.InteraccionSocial()
        case 5:
            pato = Animal_pato("pato", "5 - 10 años", "acuatico, terrestre y aereo", "peces, plantas, granos y frutas", "50-90 cm", "Varios colores")       
            pato.ImprimirDatos()
            pato.Moverse()
            pato.comunicacion()
            pato.Alimentarse()
            pato.Instinto()
            pato.Descanso()
            pato.Sueño()
            pato.InteraccionSocial()
        case 6: 
            print("Cerrando menu.....")
            break
            
    
    
    
    
    
    