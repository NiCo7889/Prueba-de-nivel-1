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
            db.vehiculo('15J', 'Marta'),
            db.vehiculo(),
            db.vehiculo()
        ]

if __name__ == '__main__':
    unittest.main()