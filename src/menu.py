# Fichero principal:
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido a tu concesionario  ")
        print("          ¿Qué desea?  ")
        print("========================")
        print("[1] coche ")
        print("[2] camioneta   ")
        print("[3] bicicleta   ")
        print("[4] motocicleta")
        print("[5] salir")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Buscando coche...\n")
        if opcion == '2':
            print("Buscando camioneta...\n")
        if opcion == '3':
            print("Añadiendo un cliente...\n")
        if opcion == '4':
            print("Modificando un cliente...\n")

        input("\nPresiona ENTER para continuar...")
