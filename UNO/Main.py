from juego.juego import Juego
from juego.jugadorAuto import jugadorAuto

def mostrarBaraja(baraja):
    print('Tus cartas:')
    n = 1

    for i in range(len(baraja)):
        carta = baraja[i]

        if carta.tipo == 'normal':
            print(str(n) + '-  ', '|', '{:<9}'.format
                (carta.color.capitalize()), 
                '{:<9}'.format(str(carta.numero)), '|', sep = '')
        else:
            print(str(n) + '-  ', '|','{:<9}'.format(carta.color.
                capitalize()), '{:<9}'.format(
                carta.poder.capitalize()), '|', sep = '')
            
        n += 1

def mostrarJuego(juego):
    if juego.juego[-1].tipo == 'normal':
        print('Última carta jugada:', '|' +
            juego.juego[-1].color.capitalize(), 
            str(juego.juego[-1].numero) + '|')
    else:
        print('Última carta jugada:', '|' + 
            juego.juego[-1].color.capitalize(), 
            juego.juego[-1].poder.capitalize() + '|')

    print('\nCartas restantes por jugador:')
    
    for i in range(len(juego.jugadores)):
        print('Jugador ' + str(i) + ':', 
            len(juego.jugadores[i].baraja))

    print()

if __name__ == '__main__':
    juego = Juego()
    finalizado = False
    
    print('Carta inicial:' + '|' + juego.juego[-1].color.
        capitalize(), str(juego.juego[-1].numero) + '|', 
        end = '\n\n')
    
    while True:
        if juego.turno == 0:
            mostrarBaraja(juego.jugadores[0].baraja)
            valida = True
            
            while True:
                if juego.verificarJuego():
                    print('\nEscriba el número de la carta que va a jugar')
                    valida = juego.jugar(input())

                    if valida: break
                    else: print('Jugada invalida, seleccione otro número')
                else:
                    print('\nArrastras de la cola\n')
                    juego.arrastrar(juego.jugadores[0])
                    mostrarBaraja(juego.jugadores[0].baraja)
                    
                    if juego.verificarJuego():
                        print('\nEscriba el número de la carta que va a jugar')
                        valida = juego.jugar(input())
                    else:
                        print('Pasas este turno\n')
                    
                    if len(juego.sobrantes) == 0:
                        juego.reordenar()
                    
                    if valida: break
                    else: print('\nJugada invalida, seleccione otro número\n')
        else:
            print('Turno del jugador automatico', juego.turno)
            juego.jugarAutomatico(juego.jugadores[juego.turno])

        mostrarJuego(juego)
        
        for i in range(4):
            if juego.verificarGanador(i):
                if i == 0:
                    print('Has ganado')
                    finalizado = True
                    break
                else:
                    finalizado = True
                    print('Has perdido, el ganador es el juegador automatico', juego.turno)
                    break
        
        if finalizado:
            break
        
        print('Presione enter para pasar al siguiente turno')

        juego.pasarTurnos()
        input()