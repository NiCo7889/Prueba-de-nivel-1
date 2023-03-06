# Fichero principal:
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido a su concesionario  ")
        print("          ¿Qué desea?  ")
        print("========================")
        print("[1] Lisatar vehículos   ")
        print("[2] Buscar vehículo   ")
        print("[3] Añadir vehículo   ")
        print("[4] Modificar vehículo   ")
        print("[5] Borrar vehículo   ")
        print("[6] Salir")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando vehículos...\n")
            for vehiculo in db.vehiculos.lista:
                print(vehiculo)

        if opcion == '2':
            print("Buscando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            vehiculo = db.vehiculos.buscar(matricula)
            print(vehiculo) if vehiculo else print("vehículo no encontrado.")

        if opcion == '3':
            print("Añadiendo vehículo...\n")
            matricula = None
            while True:
                matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
                if helpers.matricula_valida(matricula, db.vehiculos.lista):
                    break
            color = helpers.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
            ruedas = helpers.leer_texto(1, 1, "Ruedas (1 int)").capitalize()
            db.vehiculos.crear(matricula, color, ruedas)
            print("Vehículo añadido correctamente.")

        if opcion == '4':
            print("Modificando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            vehiculo = db.vehiculos.buscar(matricula)
            if vehiculo:
                color = helpers.leer_texto(
                    2, 30, f"Color (de 2 a 30 chars) [{vehiculo.color}]").capitalize()
                ruedas = helpers.leer_texto(
                    2, 30, f"Ruedas (1 int)) [{vehiculo.ruedas}]").capitalize()
                db.vehiculos.modificar(vehiculo.matricula, color, ruedas)
                print("Vehículo modificado correctamente.")
            else:
                print("Vehículo no encontrado.")

        if opcion == '5':
            print("Eliminando vehículo...\n")
            matricula = helpers.leer_texto(3, 3, "Matrícula (2 int y 1 char)").upper()
            print("Vehículo borrado correctamente.") if db.vehiculos.borrar(
                matricula) else print("Vehículo no encontrado.")
            
        if opcion == '6':
            print("Saliendo...\n")

        if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5' and opcion != '6':
            print("Opción inválida. Introduzca una opción válida.\n")


        input("\nPresiona ENTER para continuar...")