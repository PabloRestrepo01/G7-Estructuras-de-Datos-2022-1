from collections import deque
from juego.carta import Carta
from random import sample

class Juego:
    def __init__(self):
        self.mazo = deque() # Mazo de cartas
        self.torresFiguras = tuple() # Tupla que almacenará las 4 torres de figura
        self.torresFiguras += (deque(),) # Torre de figuras 1
        self.torresFiguras += (deque(),) # Torre de figuras 2
        self.torresFiguras += (deque(),) # Torre de figuras 3
        self.torresFiguras += (deque(),) # Torre de figuras 4
        self.colaArrastre = deque() # Cola de arrastre
        self.columnas = tuple() # Tupla que almacenará las 7 columnas
        self.columnas += (deque(),) # Columna 1
        self.columnas += (deque(),) # Columna 2
        self.columnas += (deque(),) # Columna 3
        self.columnas += (deque(),) # Columna 4
        self.columnas += (deque(),) # Columna 5
        self.columnas += (deque(),) # Columna 6
        self.columnas += (deque(),) # Columna 7

    def generarTipo(self, tipo, color):
        self.mazo.append(Carta(tipo, color, 1, 'A', False)) # Se añande la A al mazo
    
        for i in range(2, 11): # Se añaden las cartas del 2 al 10 al mazo
            self.mazo.append(Carta(tipo, color, i, i, False)) 
    
        self.mazo.append(Carta(tipo, color, 11, 'J', False)) # Se añande la J al mazo
        self.mazo.append(Carta(tipo, color, 12, 'Q', False)) # Se añande la Q al mazo
        self.mazo.append(Carta(tipo, color, 13, 'K', False)) # Se añande la K al mazo

    def llenarMazo(self):
        self.generarTipo('Diamantes', 'rojo') # Añado las 13 cartas de diamantes al mazo
        self.generarTipo('Corazones', 'rojo') # Añado las 13 cartas de corazones al mazo
        self.generarTipo('Picas', 'negro')     # Añado las 13 cartas de picas al mazo
        self.generarTipo('Treboles', 'negro')  # Añado las 13 cartas de treboles al mazo
        self.mazo = deque(sample(self.mazo, len(self.mazo))) # Revuelvo el mazo

    def llenarColumna(self, n):
        for i in range(n): # Añado n cartas a la columna n
            self.columnas[n - 1].append(self.mazo.pop())
        
        self.columnas[n - 1][-1].setVisible(True) # Hago visible la última carta de la columna n

    def llenarColumnas(self):
        for i in range(1, 8): # Lleno las 7 columnas
            self.llenarColumna(i)

    def destaparColaArrastre(self):
        if len(self.mazo) > 0:
            self.colaArrastre.append(self.mazo.pop()) # Añado a la cola de arrastre la que está arriba del mazo
            self.colaArrastre[-1].setVisible(True) # Hago visible la carta que está encima de la cola de arrastre

    def reiniciarColaArrastre(self):
        if len(self.mazo) == 0:
            self.mazo = self.colaArrastre
            colaArrastre = deque()
        else:
            print('Acción inválida')

    def colaATorre(self, x):
        try:
            x = int(x)
            
            if len(self.colaArrastre) > 0:
                if (len(self.torresFiguras[x - 1]) == 0 and 
                self.colaArrastre[-1].getNumero() == 1): 
                    
                    self.torresFiguras[x - 1].append(self.colaArrastre.pop())
                    
                elif (len(self.torresFiguras[x - 1]) > 0 and (self.colaArrastre[-1].getNumero() - 
                self.torresFiguras[x - 1][-1].getNumero()) == 1 and self.colaArrastre[-1].getTipo() 
                == self.torresFiguras[x - 1][-1].getTipo()):
                    
                    self.torresFiguras[x - 1].append(self.colaArrastre.pop())
                    
                else:
                    print('\nAcción inválida')
        except:
            print('\nAcción inválida')
        else:
            print('\nAcción inválida')

    def colaAColumna(self, y):
        try:
            y = int(y)
            
            if len(self.colaArrastre) > 0:
                if len(self.columnas[y - 1]) == 0 and self.colaArrastre[-1].getNumero() == 13: 
                    self.columnas[y - 1].append(self.colaArrastre.pop())
                    
                elif (len(self.columnas[y - 1]) > 0 and self.columnas[y - 1][-1].getNumero()
                - self.colaArrastre[-1].getNumero() == 1 and self.columnas[y - 1][-1].getColor()
                != self.colaArrastre[-1].getColor()):
                    
                    self.columnas[y - 1].append(self.colaArrastre.pop())
                
                else:
                    print('\nAcción inválida')
            
            else:
                print('\nAcción inválida')
        except:
            print('\nAcción inválida')

    def columnaATorre(self, x, y):
        try:
            x = int(x)
            y = int(y)
            
            if len(self.columnas[y - 1]) > 0:
                if len(self.torresFiguras[x - 1]) == 0 and self.columnas[y - 1][-1].getNumero() == 1: 
                    self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                    
                    if len(self.columnas[y - 1]) > 0:
                        self.columnas[y - 1][-1].setVisible(True)
                    
                elif (len(self.torresFiguras[x - 1]) > 0 and (self.columnas[y - 1][-1].getNumero() - 
                self.torresFiguras[x - 1][-1].getNumero()) == 1 and self.columnas[y - 1][-1].getTipo() 
                == self.torresFiguras[x - 1][-1].getTipo()) : 
                    
                    self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                    
                    if len(self.columnas[y - 1]) > 0:
                        self.columnas[y - 1][-1].setVisible(True)
                
                else:
                    print('\nAcción inválida')
            
            else:
                print('\nAcción inválida')
        except:
            print('\nAcción inválida')

    def torreAColumna(self, x, y):
        try:
            x = int(x)
            y = int(y)
            
            if len(self.torresFiguras[y - 1]) > 0:
                if len(self.columnas[x - 1]) == 0 and self.torreAColumna[y - 1][-1].getNumero() == 13: 
                    self.columnas[x - 1].append(self.torreAColumna[y - 1].pop())
                
                elif (len(self.columnas[x - 1]) > 0 and self.columnas[x - 1][-1].getNumero()
                - self.torreAColumna[y - 1][-1].getNumero() == 1 and self.columnas[x - 1][-1].getColor()
                != self.torreAColumna[y - 1][-1].getColor()):
                    
                    self.columnas[x - 1].append(self.torreAColumna[y - 1].pop())
                
                else:
                    print('\nAcción inválida')
            
            else:
                print('\nAcción inválida')
        except:
            print('\nAcción inválida')

    def columnaAColumna(self, z, x, y):
        try:
            z = int(z)
            x = int(x)
            y = int(y)
            
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
                    if len(self.columnas[y - 1]) == 0 and self.torreAColumna[x - 1][-1].getNumero() == 13: 
                        self.columnas[y - 1].extend(aux)
                        
                    elif (self.columnas[y - 1][-1].getNumero() - aux[0].getNumero() == 1 and 
                    self.columnas[y - 1][-1].getColor() != aux[0].getColor()):
                        
                        self.columnas[y - 1].extend(aux)
                        
                        if len(self.columnas[x - 1]) > 0:
                            self.columnas[x - 1][-1].setVisible(True)
                    
                    else:
                        self.columnas[x - 1].extend(aux)
                        print('\nAcción inválida')
                
                else:
                    self.columnas[x - 1].extend(aux)
                    print('\nAcción inválida')
            
            else:
                print('\nAcción inválida')
        except:
            print('\nAcción inválida')