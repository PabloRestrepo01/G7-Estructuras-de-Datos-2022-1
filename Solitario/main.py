from collections import deque
from juego.carta import Carta
from random import sample
from juego.juego import Juego

def imprimirColaArrastre(cola):
    print('Cola de arrastre' + ':', end = ' ')
    
    if len(cola) > 0:
        print('{:<9}'.format(cola[-1].getTipo()), '{:>2}'.format(cola[-1].getRepresentacion()))
    else:
        print('{:<13}'.format('Vacía'))

def imprimirTorreFiguras(torre, n):
    print('Torre de figura ' + str(n) + ':', end = ' ')
    
    if len(torre) > 0:
        print('{:<9}'.format(torre[-1].getTipo()), '{:>2}'.format(torre[-1].getRepresentacion()))
    else:
        print('{:<13}'.format('Vacía'))

def imprimirColumna(columna, n):
    print(str(n) + ':', end = '   ')
    for i in range(len(columna)):
        if columna[i].isVisible():
            print(columna[i].getTipo()[:4], '{:<2}'.format(columna[i].getRepresentacion()), end = '  ')
        else:
            print('Desc', end = '     ')
    print()

def imprimirJuego(juego):
    for i in range(4):
        imprimirTorreFiguras(juego.torresFiguras[i], i + 1)

    print()
    imprimirColaArrastre(juego.colaArrastre)
    print()
    
    for i in range(7):
        imprimirColumna(juego.columnas[i], i + 1)

if __name__ == "__main__":
    juego = Juego()
    juego.llenarMazo()
    juego.llenarColumnas()
    accion = 0
        
    while True:
        imprimirJuego(juego)
        print()
        print('Ingrese el número de la acción que desea hacer:')
        print('1. Destapar cola de arrastre')
        print('2. Reiniciar cola de arrastre')
        print('3. Llevar de cola de arrastre a Torre de figura X')
        print('4. Llevar de cola de arrastre a Columna Y')
        print('5. Llevar de Columna Y a Torre de figura X')
        print('6. Llevar de torre de figura Y a columna X')
        print('7. Llevar Z cartas de la Columna X a la columna Y')
        print('8. Salir del juego')
        
        accion = input()
        
        if accion == '1':
            juego.destaparColaArrastre()
            
        elif accion == '2':
            juego.reiniciarColaArrastre()
        elif accion == '3':
            print('Ingrese el valor de X:', end = ' ')
            x = input()
            juego.colaATorre(x)
            
        elif accion == '4':
            print('Ingrese el valor de Y:', end = ' ')
            y = input()
            juego.colaAColumna(y)
            
        elif accion == '5':
            print('Ingrese el valor de Y:', end = ' ')
            y = input()
            print('Ingrese el valor de X:', end = ' ')
            x = input()
            juego.columnaATorre(x, y)

        elif accion == '6':
            print('Ingrese el valor de Y:', end = ' ')
            y = input()
            print('Ingrese el valor de X:', end = ' ')
            x = input()
            juego.torreAColumna(x, y)
            
        elif accion == '7':
            print('Ingrese el valor de Z:', end = ' ')
            z = input()
            print('Ingrese el valor de X:', end = ' ')
            x = input()
            print('Ingrese el valor de Y:', end = ' ')
            y = input()
            juego.columnaAColumna(z, x, y)
            
        elif accion == '8':
            break
        else:
            print('\nAcción inválida')
        
        if (len(juego.torresFiguras[0]) == 13 and
        len(juego.torresFiguras[1]) == 13 and
        len(juego.torresFiguras[2]) == 13 and
        len(juego.torresFiguras[3]) == 13):
            
            print('Juego completado')
            break
        
        print()