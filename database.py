class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
    
class cliente():
    lista = []
    with open 
    




class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

c = Coche("azul", 4, 150, 1200)
print(c)

class camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return coche.__str__(self) + ", {} kg".format(self.carga)
    
class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return vehiculo.__str__(self) + ", {}".format(self.tipo)
    
class motocicleta(bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
