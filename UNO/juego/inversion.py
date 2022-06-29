from juego.carta import Carta

class Inversion(Carta):
    def __init__(self, color):
        super().__init__('especial', color)
        self.poder = 'inversion'