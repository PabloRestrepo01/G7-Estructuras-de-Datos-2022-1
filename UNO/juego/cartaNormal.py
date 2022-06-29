from juego.carta import Carta

class CartaNormal(Carta):
    def __init__(self, color, numero):
        super().__init__('normal', color)
        self.numero = numero
        