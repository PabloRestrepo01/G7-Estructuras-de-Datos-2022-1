from collections import deque
from juego.carta import Carta
from random import sample

class Juego:
    def __init__(self):
        self.mazo = deque() # Mazo de cartas.
        self.torresFiguras = tuple() # Tupla que almacenará las 4 torres de figura.
        self.torresFiguras += (deque(),) # Torre de figuras 1.
        self.torresFiguras += (deque(),) # Torre de figuras 2.
        self.torresFiguras += (deque(),) # Torre de figuras 3.
        self.torresFiguras += (deque(),) # Torre de figuras 4.
        self.colaArrastre = deque() # Cola de arrastre.
        self.columnas = tuple() # Tupla que almacenará las 7 columnas.
        self.columnas += (deque(),) # Columna 1.
        self.columnas += (deque(),) # Columna 2.
        self.columnas += (deque(),) # Columna 3.
        self.columnas += (deque(),) # Columna 4.
        self.columnas += (deque(),) # Columna 5.
        self.columnas += (deque(),) # Columna 6.
        self.columnas += (deque(),) # Columna 7.

    def generarTipo(self, tipo, color):
        self.mazo.append(Carta(tipo, color, 1, 'A', False)) # Se añande la A al mazo.
    
        for i in range(2, 11): # Se añaden las cartas del 2 al 10 al mazo.
            self.mazo.append(Carta(tipo, color, i, i, False)) 
    
        self.mazo.append(Carta(tipo, color, 11, 'J', False)) # Se añande la J al mazo.
        self.mazo.append(Carta(tipo, color, 12, 'Q', False)) # Se añande la Q al mazo.
        self.mazo.append(Carta(tipo, color, 13, 'K', False)) # Se añande la K al mazo.

    def llenarMazo(self):
        self.generarTipo('Diamantes', 'rojo') # Añado las 13 cartas de diamantes al mazo.
        self.generarTipo('Corazones', 'rojo') # Añado las 13 cartas de corazones al mazo.
        self.generarTipo('Picas', 'negro')     # Añado las 13 cartas de picas al mazo.
        self.generarTipo('Treboles', 'negro')  # Añado las 13 cartas de treboles al mazo.
        self.mazo = deque(sample(self.mazo, len(self.mazo))) # Revuelvo el mazo.

    def llenarColumna(self, n):
        for i in range(n): # Se añaden n cartas a la columna n.
            self.columnas[n - 1].append(self.mazo.pop())
        
        self.columnas[n - 1][-1].setVisible(True) # Se hace visible la última carta de la columna n.

    def llenarColumnas(self):
        for i in range(1, 8): # Se llenan las 7 columnas.
            self.llenarColumna(i)

    def destaparColaArrastre(self):
        if len(self.mazo) > 0:
            self.colaArrastre.append(self.mazo.pop()) # Se añade a la cola de arrastre la que está arriba del mazo.
            self.colaArrastre[-1].setVisible(True) # Se hace visible la carta que está encima de la cola de arrastre.
        else:
            print('Acción inválida - Mazo vacío')
            
    def reiniciarColaArrastre(self):
        if len(self.mazo) == 0: # Se verifica si el mazo está vacío.
            for i in range(len(self.colaArrastre)): # Se recorre la cola de arrastre.
                self.mazo.append(self.colaArrastre.pop()) # Se añade cada carta de la cola al mazo.
        else:
            print('Acción inválida - Mazo no vacío')

    def colaATorre(self, x):
        try:
            x = int(x)
            
            if len(self.colaArrastre) > 0: # Se verifica que hayan cartas en la cola de arrastre.
                if len(self.torresFiguras[x - 1]) == 0: # Caso 1: Se verifica que la torre de figuras
                    if self.colaArrastre[-1].getNumero() == 1: # este vacía y que la carta arriba de la cola sea un As.
                        self.torresFiguras[x - 1].append(self.colaArrastre.pop())
                    else:
                        print('\nAcción inválida - No es un As')
                    
                else:
                    if((self.colaArrastre[-1].getNumero() -  # Caso 2: Se verifica que la carta que está arriba en la 
                    self.torresFiguras[x - 1][-1].getNumero()) # torre de figuras sea mayor por 1 a la carta que está
                    == 1 and self.colaArrastre[-1].getTipo() == # arriba en la cola y que ambas sean del mismo tipo.
                    self.torresFiguras[x - 1][-1].getTipo()):
                    
                        self.torresFiguras[x - 1].append(self.colaArrastre.pop())
                    
                    else:
                        print('\nAcción inválida')
            else:
                print('\nAcción inválida - Cola de arrastre vacía')
        except:
            print('\nAcción inválida - Entrada inválida')

    def colaAColumna(self, y):
        try:
            y = int(y)
            
            if len(self.colaArrastre) > 0: # Se verifica que hayan cartas en la cola de arrastre
                if len(self.columnas[y - 1]) == 0: # Caso 1: Se verifica que
                    if (self.colaArrastre[-1].getNumero() == 13): # la columna esta vacía y que la carta que esta
                        self.columnas[y - 1].append(self.colaArrastre.pop())  # arriba de la cola es una K.
                    else:
                        print('\nAcción inválida - No es una K')
                        
                else: 
                    if (self.columnas[y - 1][-1].getNumero() # Caso 2: Se verifica que la carta que está al final de la cola
                    - self.colaArrastre[-1].getNumero() == 1 and # sea mayor por una a la de la cola de arrastre y que sean de
                    self.columnas[y - 1][-1].getColor() != self.colaArrastre[-1].getColor()): # un color diferente.
                    
                        self.columnas[y - 1].append(self.colaArrastre.pop())
                    else:
                        print('\nAcción inválida')
            
            else:
                print('\nAcción inválida - Cola de arrastre vacía')
        except:
            print('\nAcción inválida - Entrada inválida')

    def columnaATorre(self, x, y):
        try:
            x = int(x)
            y = int(y)
            
            if len(self.columnas[y - 1]) > 0: # Se verifica que la columna Y no este vacía.
                if len(self.torresFiguras[x - 1]) == 0: # Si la torre de figuras X está vacía
                    if self.columnas[y - 1][-1].getNumero() == 1: # se verifica que la carta que se le va a pasar sea un As.
                        self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                    
                        if len(self.columnas[y - 1]) > 0:
                            self.columnas[y - 1][-1].setVisible(True)
                    
                    else:
                        print('\nAcción inválida - No es un As')
                    
                else:
                    if ((self.columnas[y - 1][-1].getNumero() - # Si la columna Y no está vacía, se verifica que
                    self.torresFiguras[x - 1][-1].getNumero()) == 1 and # la diferencia entre la carta que está encima de la torre X
                    self.columnas[y - 1][-1].getTipo() == self.torresFiguras[x - 1][-1].getTipo()) : # y la que se va a pasar sea 1,
                                                                                                     # además que sean del mismo tipo.
                        self.torresFiguras[x - 1].append(self.columnas[y - 1].pop())
                    
                        if len(self.columnas[y - 1]) > 0: # Si la columna Y no queda vacía, se hace visible la carta
                            self.columnas[y - 1][-1].setVisible(True) # que queda de última.
                
                    else:
                        print('\nAcción inválida')
            
            else:
                print('\nAcción inválida - Columna vacía')
        
        except:
            print('\nAcción inválida - Entrada inválida')

    def torreAColumna(self, x, y):
        try:
            x = int(x)
            y = int(y)
            
            if len(self.torresFiguras[y - 1]) > 0: # Se verifica que la torre de figuras Y no este vacía.
                if len(self.columnas[x - 1]) == 0: # En caso de que la columna X este vacía
                    if self.torresFiguras[y - 1][-1].getNumero() == 13: # Se verifica que la carta que se va a pasar
                        self.columnas[x - 1].append(self.torresFiguras[y - 1].pop()) # sea una K.
                    else:
                        print('\nAcción inválida')
                
                else:
                    if (self.columnas[x - 1][-1].getNumero() # En caso de que la columna X no este vacía
                    - self.torresFiguras[y - 1][-1].getNumero() == 1 # se verifica que la diferencia entre
                    and self.columnas[x - 1][-1].getColor() # la última carta de X y la que se va a pasar sea 1,
                    != self.torresFiguras[y - 1][-1].getColor()): # además que sean de un color diferente.
                    
                        self.columnas[x - 1].append(self.torresFiguras[y - 1].pop())
                
                    else:
                        print('\nAcción inválida')
            
            else:
                print('\nAcción inválida - Torre de figuras vacía')
        except:
            print('\nAcción inválida - Entrada inválida')

    def columnaAColumna(self, z, x, y):
        try:
            z = int(z)
            x = int(x)
            y = int(y)
            
            aux = deque() # Cola auxiliar
            valida = True
            
            if len(self.columnas[x - 1]) >= z: # Se verifica que la columna tenga mas de Z cartas.
                for i in range(z): # Se añaden las últimas Z cartas de la columna en la cola auxiliar.
                    if self.columnas[x - 1][-1].isVisible(): # Se verifica que las Z cartas sean visibles
                        aux.appendleft(self.columnas[x - 1].pop()) # De lo contrario la acción será invalida.   
                    else:
                        valida = False
                        break
        
                if valida:
                    if len(self.columnas[y - 1]) == 0: # En el caso que la columna Y este vacía se verifica
                        if aux[0].getNumero() == 13:   # que el primer valor que se le pase sea una K.
                            self.columnas[y - 1].extend(aux)
                            
                            if len(self.columnas[x - 1]) > 0: # En caso de que la columna X no quede vacía
                                self.columnas[x - 1][-1].setVisible(True) # se hace visible la carta que queda de última.
                        
                    elif (self.columnas[y - 1][-1].getNumero() - aux[0].getNumero() == 1 and # En caso de que la columna Y no
                    self.columnas[y - 1][-1].getColor() != aux[0].getColor()):  # este vacía se verifica que la diferencia entre
                                                                                # la ultima carta de Y con el primer valor que se
                        self.columnas[y - 1].extend(aux)                        # le pase sea 1 y que sean de colores diferentes.
                        
                        if len(self.columnas[x - 1]) > 0: # En el caso de que la columna X no quede vacía
                            self.columnas[x - 1][-1].setVisible(True) # se hace visible la carta que queda de última.
                    
                    else:
                        self.columnas[x - 1].extend(aux) # En caso de no ser posible pasar las cartas de aux a la columna Y,
                        print('\nAcción inválida') # estas retornan a X.
                
                else:
                    self.columnas[x - 1].extend(aux) # En caso de no ser posible pasar las cartas de aux a la columna Y,
                    print('\nAcción inválida') # estas retornan a X.
            
            else:
                print('\nAcción inválida')
        except:
            print('\nAcción inválida - Entrada inválida')