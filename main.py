diccionari = {
    "xarxa": {
        "PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal, anomenada malla. Són anomenades filats i, preferentment, arts.",
        "TÈXTIL": "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà, de cànem, de lli o, modernament, de niló.",
    },
    "informàtica": {
        "TECNOLOGIA": "Conjunt de ciències, tècniques o activitats relacionades amb el tractament automatitzat de dades. Informàtica de gestió. Informàtica d’oficina.",
        "NÚVOL": "Organització d’un sistema informàtic en què l’usuari fa ús de recursos i serveis de processament i emmagatzematge de dades allotjats en servidors externs accessibles a través d’internet.",
    },
    "acrònim": {
        "NOM": "Qualsevol abreviació formada amb lletres o segments inicials o finals extrets dels mots que componen una frase, que és pronunciable com un mot ordinari; per exemple, radar, làser, UNESCO, etc."
    },
}

opcio1=-1
import os
import msvcrt
import cowsay
from pydub import AudioSegment
from pydub.playback import play
cls = lambda: os.system('cls')
cls()
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
    
#Afegir

def afegir():
    cls()
    print( "Has escollit Afegir")
    key = input("Introdueix una paraula: ")
    key2= input("Introdueix una especificacio: ")
    value = input("Introdueix el seu significat: ")
    diccionari.update({key:{key2:value}})
    cls()
    
#Mostrar

def mostrar():
    cls()
    print("Has escollit Mostrar")
    for categoria in diccionari.keys():
        print(categoria)
    categoria=input("Insertar una categoria a consultar: ")
    cls()
    print("Has escogido ",categoria,"")
    for palabra,definicion in diccionari[categoria].items():
        print("- ",palabra," : ",definicion,"")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
#Modificar

def modificar():
    cls()
    print("Has escollit Modificar")
    for categoria in diccionari.keys():
        print(categoria)
    opcioncategoria=input("Que quieres modificar: ")
    cls()
    print("Has escogido ",opcioncategoria,"")
    print("1 Si")
    print("2 No")
    elecion=int(input("Quieres modificar la categoria? "))
    match elecion:
        case 1:
            original=opcioncategoria
            modificacion=input("Introduece la categoria: ")
            diccionari[modificacion]=diccionari.pop(original)
        case 2:
            for palabra,definicion in diccionari[opcioncategoria].items():
                print("- ",palabra," : ",definicion,"")
            opcion2=input("Que termino quieres cambiar: ")
            print("1 Si")
            print("2 No")
            elecion2=int(input("Quieres modificar el termino: "))
            match elecion2:
                case 1:
                    original2=opcion2
                    modificacion2=input("Nuevo nombre: ")
                    definicion=diccionari[opcioncategoria].pop(original2)
                    diccionari[opcioncategoria][modificacion2]=definicion
                case 2:
                    print("1 Si")
                    print("2 No")
                    elecion3=int(input("Quieres modificar el significado: "))
                    match elecion3:
                        case 1:
                            termino=opcion2
                            nuevadefinicion=input("Introduce la nueva modificacion: ")
                            diccionari[opcioncategoria][termino] = nuevadefinicion
            
#Eliminar

def eliminar():
    cls()
    print("Has escollit eliminar")
    for categoria in diccionari.keys():
        print(categoria)
    opcioncategoria=input("Que quieres eliminar: ")
    print("1 Si")
    print("2 No")
    elecion=int(input("Quieres eliminar esta categoria: "))
    match elecion:
        case 1:
            diccionari.pop(opcioncategoria)
        case 2:
            for palabra,definicion in diccionari[opcioncategoria].items():
                print("- ",palabra," : ",definicion,"")
            opcion=input("Que termino quieres eliminar: ")
            print("1 Si")
            print("2 No")
            elecion2=int(input("Quieres eliminar este termino? "))
            match elecion2:
                case 1:
                    definicion=diccionari[opcioncategoria].pop(opcion)
                

while opcio1 != 5:
    cls()
    opcio1=menu()
    match opcio1:
        case 1:
            afegir()
        case 2:
            mostrar()
        case 3 :
            modificar()
        case 4 :
            eliminar()
cowsay.cow("JOSEP GUAPO APRUEBAME PITON")
sound = AudioSegment.from_file("mecorro.wav", format="wav")
play(sound)