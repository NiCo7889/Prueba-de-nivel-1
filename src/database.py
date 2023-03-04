class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
    def to_dict(self): 
        return {'color': self.color, 'ruedas': self.ruedas}