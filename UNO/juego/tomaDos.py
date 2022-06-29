from juego.carta import Carta

class TomaDos(Carta):
    def __init__(self, color):
        super().__init__('especial', color)
        self.poder = 'toma 2'