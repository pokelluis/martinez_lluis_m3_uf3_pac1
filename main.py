diccionari = {}
opcio1=0
import os
clear = lambda: os.system('cls')

print("\n----------------------------------------")
print("Benvingut a El Llibre de les Acceptions.")
print("----------------------------------------\n\n")

#MenuOpcions
print("Que vols fer? \n\n")
print("1.Afegir")
print("2.Mostrar")
print("3.Modificar")
print("4.Eliminar")
while opcio1 < 0 and opcio1 > 4:
    opcio1 = input("Introdueix una opcio valida")


match :
    case 1:
        return "Has escollit Afegir"
        cls()
        clau = input("Introdueix una paraula:")
        valor = input("Introdueix el seu significat")
    case 2:
        return "Has escollit Mostrar"
    case 3:
        return "Has escollit Modificar"
    case 4:
        return "Has escollit Eliminar"
    default:
        return "desconocido"