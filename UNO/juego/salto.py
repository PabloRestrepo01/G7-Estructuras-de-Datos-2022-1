from juego.carta import Carta

class Salto(Carta):
    def __init__(self, color):
        super().__init__('especial', color)
        self.poder = 'salto'