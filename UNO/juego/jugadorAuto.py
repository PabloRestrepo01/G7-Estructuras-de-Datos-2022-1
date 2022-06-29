from juego.jugador import Jugador

class jugadorAuto(Jugador):
    def __init__(self):
        super().__init__()
    
    def jugarA(self,carta):
        for i in range(len(self.baraja)):
            retorno = self.baraja[i]
            
            if (self.baraja[i].tipo == 'especial' and
                carta.tipo == 'especial'):
                
                if self.baraja[i].poder == carta.poder:
                    self.baraja.pop(i)
                    return retorno
            
            elif self.baraja[i].color == carta.color:
                self.baraja.pop(i)
                return retorno
                
            elif (self.baraja[i].tipo == 'normal' and
                carta.tipo == 'normal'):
                
                if self.baraja[i].numero == carta.numero:
                    self.baraja.pop(i)
                    return retorno
            
        return False