import csv
import config


class vehiculo():
    def __init__(self, matricula, color, ruedas):
        self.matricula = matricula
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.matricula, self.color, self.ruedas )
    
    def to_dict(self): 
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas}
    

class coche(vehiculo):
    def __init__(self, matricula, color, ruedas, velocidad, cilindrada):
        super().__init__(matricula, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}
    

class bicicleta(vehiculo):
    def __init__(self, matricula, color, ruedas, tipo):
        super().__init__(matricula, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return vehiculo.__str__(self) + ", {}".format(self.tipo)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'tipo': self.tipo}


class camioneta(coche):
    def __init__(self, matricula, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(matricula, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return coche.__str__(self) + ", {} kg".format(self.carga)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'velocidad': self.velocidad, 'cilindrada': self.cilindrada, 'carga': self.carga}

class fórmula1(coche):
    def __init__(self, matricula, color, ruedas, velocidad, cilindrada, equipo):
        super().__init__(matricula, color, ruedas, velocidad, cilindrada)
        self.equipo = equipo

    def __str__(self):
        return coche.__str__(self) + ", {}".format(self.equipo)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'velocidad': self.velocidad, 'cilindrada': self.cilindrada, 'equipo': self.equipo}

class motocicleta(bicicleta):
    def __init__(self, matricula, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(matricula, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'tipo': self.tipo, 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}    

class quad(coche, bicicleta):
    def __init__(self, matricula, color, ruedas, velocidad, cilindrada, tipo, modelo, carga):
        super().__init__(matricula, color, ruedas, velocidad, cilindrada)
        self.tipo = tipo
        self.modelo = modelo
        self.carga = carga

    def __str__(self):
        return bicicleta.__str__(self) + ", {} km/h, {}cc, {}, {}".format(self.velocidad, self.cilindrada, self.modelo, self.carga)
    
    def to_dict(self):
        return {'matricula': self.matricula, 'color': self.color, 'ruedas': self.ruedas, 'velocidad': self.velocidad, 'cilindrada': self.cilindrada, 'tipo': self.tipo, 'modelo': self.modelo, 'carga': self.carga}    

class vehiculos():
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for matricula, color, ruedas in reader:
            vehiculo = vehiculo(matricula, color, ruedas)
            lista.append(vehiculo)

    @staticmethod
    def catalogar():
        for vehiculo in vehiculos.lista:
            print("{} {}".format(type(vehiculo).__name__, vehiculo))
    @staticmethod
    def buscar(matricula):
        for vehiculo in vehiculos.lista:
            if vehiculo.matricula == matricula:
                return vehiculo

    @staticmethod
    def crear(matricula, color, ruedas):
        vehiculo = vehiculo(matricula, color, ruedas)
        vehiculos.lista.append(vehiculo)
        vehiculos.guardar()
        return vehiculo

    @staticmethod
    def modificar(matricula, color, ruedas):
        for indice, vehiculo in enumerate(vehiculos.lista):
            if vehiculo.matricula == matricula:
                vehiculos.lista[indice].color = color
                vehiculos.lista[indice].ruedas = ruedas
                vehiculos.guardar()
                return vehiculos.lista[indice]

    @staticmethod
    def borrar(matricula):
        for indice, vehiculo in enumerate(vehiculos.lista):
            if vehiculo.matricula == matricula:
                vehiculo = vehiculos.lista.pop(indice)
                vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in vehiculos.lista:
                writer.writerow((vehiculo.matricula, vehiculo.color, vehiculo.ruedas))






    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for color, ruedas, velocidad, cilindrada, tipo, modelo, carga, equipo in reader:
            if velocidad == '':
                velocidad = 0
            if cilindrada == '':
                cilindrada = 0
            if carga == '':
                carga = 0
            if tipo == '':
                tipo = 'no tiene'
            if modelo == '':
                modelo = 'no tiene'
            if equipo == '':
                equipo = 'no tiene'
            lista.append([color, ruedas, velocidad, cilindrada, tipo, modelo, carga, equipo])

    @staticmethod
    def catalogar():
        for vehiculo in vehiculos.lista:
            print(vehiculo)
            ruedas = vehiculo.ruedas
            if ruedas == 0:
                print("No es posible que un vehículo no tenga ruedas")
            elif ruedas == 2:
                print("Es una bicicleta")
            elif ruedas == 4:
                print("Es un coche")
            return vehiculos.lista
        



        lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
# utilizo los decoradores @staticmethod para poder acceder a los métodos sin necesidad de crear un objeto de tipo Clientes
    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))