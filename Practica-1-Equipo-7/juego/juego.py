from collections import deque
from juego.carta import Carta
from random import sample

class Juego:
    def __init__(self):
        self.mazo = deque()
        self.torresFiguras = tuple()
        self.torresFiguras += (deque(),) # Torre de figuras 1
        self.torresFiguras += (deque(),) # Torre de figuras 2
        self.torresFiguras += (deque(),) # Torre de figuras 3
        self.torresFiguras += (deque(),) # Torre de figuras 4
        self.colaArrastre = deque()
        self.columnas = tuple()
        self.columnas += (deque(),) # Columna 1
        self.columnas += (deque(),) # Columna 2
        self.columnas += (deque(),) # Columna 3
        self.columnas += (deque(),) # Columna 4
        self.columnas += (deque(),) # Columna 5
        self.columnas += (deque(),) # Columna 6
        self.columnas += (deque(),) # Columna 7
    
    def generarTipo(self, tipo, color):
        self.mazo.append(Carta(tipo, color, 1, 'A', False))
    
        for i in range(2, 11):
            self.mazo.append(Carta(tipo, color, i, i, False))
    
        self.mazo.append(Carta(tipo, color, 11, 'J', False))
        self.mazo.append(Carta(tipo, color, 12, 'Q', False))
        self.mazo.append(Carta(tipo, color, 13, 'K', False))
    
    def llenarCola(self):
        self.generarTipo('Diamantes', 'rojo') # Añado las 13 cartas de diamantes a la cola de arrastre
        self.generarTipo('Corazones', 'rojo') # Añado las 13 cartas de corazones a la cola de arrastre
        self.generarTipo('Picas', 'negro')     # Añado las 13 cartas de picas a la cola de arrastre
        self.generarTipo('Treboles', 'negro')  # Añado las 13 cartas de treboles a la cola de arrastre
        self.mazo = deque(sample(self.mazo, len(self.mazo)))
    
    def llenarColumna(self, columna):
        for i in range(columna):
            self.columnas[columna - 1].append(self.mazo.pop())
        
        self.columnas[columna - 1][-1].setVisible(True)
    
    def llenarColumnas(self):
        for i in range(1, 8):
            self.llenarColumna(i)
    
    def destaparColaArrastre(self):
        if len(self.mazo) > 0:
            self.colaArrastre.append(self.mazo.pop())
            self.colaArrastre[-1].setVisible(True)
    
    def colaATorre(self, x):
        if len(self.colaArrastre) > 0:
            if len(self.torresFiguras[x - 1]) == 0 and self.colaArrastre[-1].getNumero() == 1: 
                self.torresFiguras[x - 1].append(self.colaArrastre.pop())
            elif (len(self.torresFiguras[x - 1]) > 0 and (self.colaArrastre[-1].getNumero() - self.torresFiguras[x - 1][-1]) == 1
                and self.colaArrastre[-1].getTipo() == self.torresFiguras[x - 1][-1].getTipo()) : 
                self.torresFiguras[x - 1].append(self.colaArrastre.pop())
            else:
                print('Acción inválida')
        else:
            print('Acción inválida')

    def colaAColumna(self, y):
        if len(self.colaArrastre) > 0:
            if len(self.columnas[y - 1]) == 0 and self.colaArrastre[-1].getNumero() == 13: 
                self.columnas[y - 1].append(self.colaArrastre.pop())
            elif (len(self.columnas[y - 1]) > 0 and self.columnas[y - 1][-1].getNumero()
            - self.colaArrastre[-1].getNumero() == 1 and self.columnas[y - 1][-1].getColor()
            != self.colaArrastre[-1].getColor()):
                self.columnas[y - 1].append(self.colaArrastre.pop())
            else:
                print('Acción inválida')
        else:
            print('Acción inválida')

    def columnaATorre(self, x, y):
        if len(self.columnas[y - 1]) > 0:
            if len(self.torresFiguras[x - 1]) == 0 and self.columnas[y - 1][-1].getNumero() == 1: 
                self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                
                if len(self.columnas[y - 1]) > 0:
                    self.columnas[y - 1][-1].setVisible(True)
                
            elif (len(self.torresFiguras[x - 1]) > 0 and (self.self.columnas[y - 1].getNumero() - self.torresFiguras[x - 1][-1]) == 1
            and self.columnas[y - 1][-1].getTipo() == self.torresFiguras[x - 1][-1].getTipo()) : 
                self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                
                if len(self.columnas[y - 1]) > 0:
                    self.columnas[y - 1][-1].setVisible(True)
            else:
                print('Acción inválida')
        else:
            print('Acción inválida')

    def torreAColumna(self, x, y):
        if len(self.torresFiguras[y - 1]) > 0:
            if len(self.columnas[x - 1]) == 0 and self.torreAColumna[y - 1][-1].getNumero() == 13: 
                self.columnas[x - 1].append(self.torreAColumna[y - 1].pop())
            elif (len(self.columnas[x - 1]) > 0 and self.columnas[x - 1][-1].getNumero()
            - self.torreAColumna[y - 1][-1].getNumero() == 1 and self.columnas[x - 1][-1].getColor()
            != self.torreAColumna[y - 1][-1].getColor()):
                self.columnas[x - 1].append(self.torreAColumna[y - 1].pop())
            else:
                print('Acción inválida')
        else:
            print('Acción inválida')
    
    def columnaAColumna(self, z, x, y):
        aux = deque()
        valida = True
        if len(self.columnas[x - 1]) >= z:
            for i in range(z):
                if self.columnas[x - 1][-1].isVisible():
                    aux.appendleft(self.columnas[x - 1].pop())
                else:
                    valida = False
                    break
    
            if valida:
                if (self.columnas[y - 1][-1].getNumero() - aux[0].getNumero() == 1 and self.columnas[y - 1][-1].getColor()
                != aux[0].getColor()):
                    self.columnas[y - 1].extend(aux)
                    self.columnas[x - 1][-1].setVisible(True)
                else:
                    self.columnas[x - 1].extend(aux)
                    print('Acción inválida')
            else:
                self.columnas[x - 1].extend(aux)
                print('Acción inválida')
        else:
            print('Acción inválida')