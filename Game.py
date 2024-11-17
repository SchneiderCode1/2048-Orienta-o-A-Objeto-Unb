from package import *

jogada = ProxJogada()
EndGame = FimDeJogo()

jogada.RandomPos()
jogada.PrintBoard()

p = 1

while p == 1:
    proxima_jogada = int(input("digite 1 para subir todas as linhas:\n"))

    if proxima_jogada == 1:
        jogada.SomaUp()
    
    jogada.PrintBoard()
    jogada.RandomPos()
    terminar_jogo = int(input("Para terminar digite 0\n"))
    
    if terminar_jogo == 0:
        p == 0
    else:
        pass

    jogada.PrintBoard()
