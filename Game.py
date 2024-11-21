from package import *
import colorama

jogada = ProxJogada()
fim = FimDeJogo()

jogada.RandomPos()
jogada.PrintBoard()

p = 1

while p == 1:
    fim.Fim()
    if fim.endGame:
        print("Fim de Jogo")
        break
    
    if jogada.endGame:
        print("Fim de jogo!")
        break
        
        
    proxima_jogada = input("""
            +---+
            | w |
        +---+---+---+
        | a | s | d |
        +---+---+---+

    Digite sua jogada (w/cima, s/baixo, a/esquerda, d/direita) ou 0 para sair: 
    """).lower()

    if proxima_jogada == "w":
        jogada.SomaUp()
        
    elif proxima_jogada == "s":
        jogada.SomaDown()
        
    elif proxima_jogada == "a":
        jogada.SomaLeft()
        
    elif proxima_jogada == "d":
        jogada.SomaRight()
        
    elif proxima_jogada == 0:
        p == 0
    
    else:
        print("Digite uma jogada válida:\n")
    
    jogada.PrintBoard()
    jogada.RandomPos()
    jogada.PrintBoard()
    
