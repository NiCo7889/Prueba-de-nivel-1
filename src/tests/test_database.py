import csv
import copy
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.vehiculos.lista = [
            db.coche("36", "amarillo", 150, 150),
            db.camioneta("45H", "rosa", 130, 160, 1000),
            db.fórmula1("24E", "rojo", 400, 1600, "AstonMartin"),
            db.quad("quad", "93V", "verde", 100, 200, 500, "urbana", 700),
        ]

    def test_catalogar(self):
        # Prueba 1
        lista = db.vehiculos.catalogar()
        self.assertEqual(len(lista), 3)
        # Prueba 2
        lista = db.vehiculos.catalogar(2)
        self.assertEqual(len(lista), 1)
        # Prueba 3
        lista = db.vehiculos.catalogar(4)
        self.assertEqual(len(lista), 2)
    
    def test_buscar(self):
        # Prueba 1
        vehiculo = db.vehiculos.buscar("1234")
        self.assertEqual(vehiculo, None)
        # Prueba 2
        vehiculo = db.vehiculos.buscar("1234", 2)
        self.assertEqual(vehiculo, None)
        # Prueba 3
        vehiculo = db.vehiculos.buscar("1234", 4)
        self.assertEqual(vehiculo, None)
        # Prueba 4
        vehiculo = db.vehiculos.buscar("1234", 1)
        self.assertEqual(vehiculo, db.vehiculos.lista[0])
        # Prueba 5
        vehiculo = db.vehiculos.buscar("1234", 3)
        self.assertEqual(vehiculo, db.vehiculos.lista[2])
        # Prueba 6
        vehiculo = db.vehiculos.buscar("1234", 2)
        self.assertEqual(vehiculo, db.vehiculos.lista[1])

    def test_crear(self):
        # Prueba 1
        vehiculo = db.vehiculos.crear("1234", "Rojo", 4)
        self.assertEqual(vehiculo, db.vehiculos.lista[3])
        # Prueba 2
        vehiculo = db.vehiculos.crear("1234", "Rojo", 4)
        self.assertEqual(vehiculo, None)
        # Prueba 3
        vehiculo = db.vehiculos.crear("1234", "Rojo", 4)
        self.assertEqual(vehiculo, None)

    def test_modificar(self):
        # Prueba 1
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, None)
        # Prueba 2
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, None)
        # Prueba 3
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, None)
        # Prueba 4
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, db.vehiculos.lista[0])
        # Prueba 5
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, db.vehiculos.lista[1])
        # Prueba 6
        vehiculo = db.vehiculos.modificar("1234", "Rojo", 4)
        self.assertEqual(vehiculo, db.vehiculos.lista[2])

    def test_borrar(self):
        # Prueba 1
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, None)
        # Prueba 2
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, None)
        # Prueba 3
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, None)
        # Prueba 4
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, db.vehiculos.lista[0])
        # Prueba 5
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, db.vehiculos.lista[1])
        # Prueba 6
        vehiculo = db.vehiculos.borrar("1234")
        self.assertEqual(vehiculo, db.vehiculos.lista[2])

    def test_guardar(self):
        # Prueba 1
        db.vehiculos.guardar()
        with open(config.DATABASE_PATH, "r") as file:
            reader = csv.reader(file)
            lista = list(reader)
            self.assertEqual(len(lista), 3)
        # Prueba 2
        db.vehiculos.guardar()
        with open(config.DATABASE_PATH, "r") as file:
            reader = csv.reader(file)
            lista = list(reader)
            self.assertEqual(len(lista), 3)
        # Prueba 3
        db.vehiculos.guardar()
        with open(config.DATABASE_PATH, "r") as file:
            reader = csv.reader(file)
            lista = list(reader)
            self.assertEqual(len(lista), 3)