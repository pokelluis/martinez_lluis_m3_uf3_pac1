diccionari = {}
opcio1=-1
import os
cls = lambda: os.system('cls')

print("\n----------------------------------------")
print("Benvingut a El Llibre de les Acceptions.")
print("----------------------------------------\n\n")

#MenuOpcions
def menu():
    print("Que vols fer? \n\n")
    print("1.Afegir")
    print("2.Mostrar")
    print("3.Modificar")
    print("4.Eliminar")
    print("5.Salir")
    opcio1 = int(input("\n\nIntrodueix una opcio valida: "))
    return opcio1
    
while opcio1 != 5:
    opcio1=menu()
    match opcio1:
        case 1:
            cls()
            print( "Has escollit Afegir")
            clau = input("Introdueix una paraula: ")
            valor = input("Introdueix el seu significat: ")
            diccionari.update({clau:valor})
        case 2:
            cls()
            num = 1
            print("Has escollit Mostrar")
            for i in diccionari.keys():
                print(num ," : ", i)
            if 
            