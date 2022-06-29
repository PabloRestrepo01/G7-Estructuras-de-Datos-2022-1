from collections import deque
from random import sample
from random import randint
from juego.cartaNormal import CartaNormal
from juego.jugadorAuto import jugadorAuto
from juego.salto import Salto
from juego.inversion import Inversion
from juego.tomaDos import TomaDos
from juego.jugador import Jugador
from juego.jugadorAuto import jugadorAuto

class Juego:
    def __init__(self):
        self.sobrantes = deque() # Genero un mazo vacío que será una pila de cartas
        self.llenarSobrantes() # Lleno el mazo
        self.jugadores = (Jugador(), jugadorAuto(), 
                        jugadorAuto(), jugadorAuto()) # Creo los 4 jugadores
        
        self.generarBarajas() # Le genero a cada jugador una baraja
        self.turno = randint(0, 3) # El primer turno se asignará aleatoriamente
        self.sentido = 1 # El sentido será 1 si el juego va a en sentido horario o -1 de lo contrario
        self.juego = deque() # Inicializo el juego principal que será una pila
        self.iniciarJuego() # Le agrego al juego principal la primera carta de la pila de sobrantes
        self.acumulador = 2 # Número de cartas que se toman al recibir una serie de "Toma 2"
        
    def llenarSobrantes(self):
        colores = ('amarillo', 'azul', 'rojo', 'verde')
        
        for i in range(len(colores)): # Genero las 10 cartas numericas por color dos veces
            for j in range(1, 10):
                self.sobrantes.append(CartaNormal(colores[i], j))
                self.sobrantes.append(CartaNormal(colores[i], j))

            # Genero las cartas especiales para cada color
            self.sobrantes.append(Salto(colores[i]))
            self.sobrantes.append(Salto(colores[i]))
            self.sobrantes.append(Inversion(colores[i]))
            self.sobrantes.append(Inversion(colores[i]))
            self.sobrantes.append(TomaDos(colores[i]))
            self.sobrantes.append(TomaDos(colores[i]))
        
        self.sobrantes = deque(sample(self.sobrantes, 
                            len(self.sobrantes))) # Revuelvo el mazo

    def iniciarJuego(self): # Inicio el juego y controlo que no sea con una carta especial
        while True:
            if self.sobrantes[-1].tipo == 'normal':
                self.juego.append(self.sobrantes[-1])
                break
            else:
                self.sobrantes.appendleft(self.sobrantes.pop())
                
    def generarBarajas(self): # Asigno a cada uno de los 4 jugadores 8 cartas
        for i in range(4):
            for j in range(8):
                carta = self.sobrantes.pop()
                self.jugadores[i].baraja.append(carta)

    def verificarJuego(self): # Verifico si el jugador humano tiene cartas para jugar
        jugadorHumano = self.jugadores[0]
        
        for i in range(len(self.jugadores[0].baraja)):
            if jugadorHumano.baraja[i].color == self.juego[-1].color:
                return True
            
            if (self.juego[-1].tipo == 'especial' and
            jugadorHumano.baraja[i].tipo == 'especial'):
                
                if self.juego[-1].poder == jugadorHumano.baraja[i].poder:
                    return True
            
            elif (self.juego[-1].tipo == 'normal' and
            jugadorHumano.baraja[i].tipo == 'normal'):
                
                if self.juego[-1].numero == jugadorHumano.baraja[i].numero:
                    return True
            
        return False
        
    def jugar(self, n): # Jugar la carta n - 1, donde n es ingresada por el jugador humano
        try:
            n = int(n)
            carta = self.jugadores[0].baraja[n - 1]
            color = carta.color
            
            if (carta.tipo == 'normal' and 
                self.juego[-1].tipo == 'normal'):
                
                numero = carta.numero
                
                if (color == self.juego[-1].color or
                    numero == self.juego[-1].numero):
                    
                    self.juego.append(carta)
                    self.jugadores[0].baraja.remove(carta)
                    self.especiales()
                    return True
            
            elif (carta.tipo == 'especial' and
                self.juego[-1].tipo == 'especial'):
                
                poder = carta.poder
                
                if (color == self.juego[-1].color or
                    poder == self.juego[-1].poder):
                    
                    self.juego.append(carta)
                    self.jugadores[0].baraja.remove(carta)
                    self.especiales()
                    return True
            
            else:
                if color == self.juego[-1].color:
                    self.juego.append(carta)
                    self.jugadores[0].baraja.remove(carta)
                    self.especiales()
                    return True
                
            return False
        
        except:
            return False
    
    def jugarAutomatico(self, jugador):
        
        retorno = jugador.jugarA(self.juego[-1])
        
        if retorno != False:
            self.juego.append(retorno)

            self.especiales()
        else:
            print('El jugador arrastra de la cola')
            
            self.arrastrar(jugador)
            retorno = jugador.jugarA(self.juego[-1])
        
            if retorno != False:
                self.juego.append(retorno)

                self.especiales()
            else:
                print('El jugador pasa este turno\n')
                
            if len(self.sobrantes) == 0:
                self.reordenar()
        
    def especiales(self):
        if self.juego[-1].tipo == 'especial':
            if self.juego[-1].poder == 'inversion':
                self.inversion()
            
            elif self.juego[-1].poder == 'toma 2':
                self.responder()
                self.tomaDos()
                self.acumulador = 2
            
            elif self.juego[-1].poder == 'salto':
                self.responder()
                self.salto()
                
    def pasarTurnos(self):
        if self.sentido == 1:
            if self.turno == len(self.jugadores) - 1:
                self.turno = 0
            else:
                self.turno += 1
        
        else:
            if self.turno == 0:
                self.turno = len(self.jugadores) - 1
            else:
                self.turno -= 1

    def salto(self):
        self.pasarTurnos()
    
    def inversion(self):
        self.sentido *= -1
    
    def tomaDos(self):
        self.pasarTurnos()
        for i in range(self.acumulador):
            self.jugadores[self.turno].baraja.append(self.sobrantes.pop())
    
    def arrastrar(self, jugador):
        jugador.baraja.append(self.sobrantes.pop())

    def reordenar(self):
        self.sobrantes = deque(sample(self.juego[:-1], len(self.juego) - 1))
        self.juego = self.juego[-1]
    
    def verificarGanador(self, i):
        if len(self.jugadores[i].baraja) == 0:
            return True
        return False

    def responder(self):
        t = self.turno

        while True:
            if self.sentido == 1:
                if t == len(self.jugadores) - 1:
                    t = 0
                else:
                    t += 1
            
            else:
                if t == 0:
                    t = len(self.jugadores) - 1
                else:
                    t -= 1
            
            if self.buscarPoder(self.jugadores[t], self.juego[-1], t):
                self.turno = t
                if self.juego[-1].poder == 'toma 2':
                    self.acumulador += 2
                
                if t != 0:
                    print('\nEl jugador automatico', t, 'respondió al poder')
                else:
                    print('\nRespondiste al poder')
            else:
                return False
            
    def buscarPoder(self, jugador, carta, t):
        for i in range(len(jugador.baraja)):
            if jugador.baraja[i].tipo == 'especial':
                if jugador.baraja[i].poder == carta.poder:
                    print('Última carta jugada: |' + 
                        self.juego[-1].color.capitalize(),
                        self.juego[-1].poder.capitalize() +'|')
                            
                    if t != 0:
                        self.juego.append(jugador.baraja.pop(i))
                        return True
                    else:
                        print('\nTus cartas:')
                        n = 1
                        for i in range(len(self.jugadores[0].baraja)):
                            car = self.jugadores[0].baraja[i]

                            if car.tipo == 'normal':
                                print(str(n) + '-  ', '|', '{:<9}'.format
                                    (car.color.capitalize()), 
                                    '{:<9}'.format(str(car.numero)), '|', sep = '')
                            else:
                                print(str(n) + '-  ', '|','{:<9}'.format(car.color.
                                    capitalize()), '{:<9}'.format(
                                    car.poder.capitalize()), '|', sep = '')
                            
                            n += 1
                        
                        valida = False
                        
                        while not valida:
                            print('\nResponde al poder:')
                            ncarta = input()
                            c = carta.poder
                            
                            try:
                                ncarta = int(ncarta)
                                if self.jugadores[0].baraja[ncarta - 1].tipo == 'especial':
                                    if self.jugadores[0].baraja[ncarta - 1].poder == c:
                                        self.juego.append(self.jugadores[0].baraja.pop(ncarta - 1))
                                        valida = True
                                        break
                                    else:
                                        print('Jugada invalida')
                                else:
                                    print('Jugada invalida')
                            except:
                                print('Jugada invalida')
                                
                        return True
        return False