from package import *
import json
import time 

novo_save = NovoSave()
carregar_save = CarregarSave()

Jogo = True



while True:
    entrada = int(input("Bem Vindo!\nEsse é um jogo chamado 2048.\nSelecione uma opção para continuar:\n1 - Novo Jogo\n2 - Carregar jogo salvo\n3 - Regras\n4 - Escolher um save para remover (WIP)\n\n"))
    if entrada == 1: # Novo Jogo 
        print("Vamos iniciar o jogo!")
        nome_save = str(input("Qual será o nome do seu Save? Ex:. save_1 :\n"))
        taman = int(input("Qual é será1 o tamanho da sua grade de jogo? Ex:. 5 -> 5x5 : \n"))
        novo_save.create_save(taman, nome_save)
        grade_jogo = [0] * (taman**2)
        
        print(nome_save)
        
        save = SalvarJogo(grade_jogo, nome_save, taman)
        remove = RemoverJogo(grade_jogo, nome_save, taman)
        
        break

    elif entrada == 2:#Carregar Jogo
        carregar_save.saves_disponiveis()
        num = int(input("Selecione o número do save que você deseja carregar:.\n"))
        grade_jogo = carregar_save.load_save(num)
        nome_save = carregar_save.pegar_nome_save()
        
        save = SalvarJogo(grade_jogo, nome_save)
        remove = RemoverJogo(grade_jogo, nome_save)
        
        taman = carregar_save.SaveGames[nome_save]["grade"]
        
        break

    elif entrada == 3: #Regras
        entrada = 0
        print("Regras:\nO objetivo do jogo é chegar ao número 2048.\nCada movimento leva todos os elementos da grade até a borda e soma os números iguais, Ex:. 2 + 2 + 2 + 2 = 4 + 4 = 8.\nCada movimento adiciona um número 2 ou 4 em uma posição vazia aleatória.\n")
    
    elif entrada == 4: #Escolher um save para remover WIP
        carregar_save.saves_disponiveis()
        num = int(input("Selecione o número do save que você deseja remover:.\n"))
        
        nome_save = carregar_save.pegar_nome_save()
        grade_jogo = carregar_save.load_save(num)
        
        remove = RemoverJogo(grade_jogo, nome_save)
        while True:
            inp = int(input("Você tem certeza de que quer apagar esse save? Não tem volta!\n1 - Sim\n2 - Não\n"))
            if inp == 1:
                remove.apagar_jogo()
                print("Apagado!")
            if inp == 2:
                break
    
    else:
        print("Digite um número válido")


grade_numerica= GradeNum(taman) #cria o objeto de grade Numerica
grade = Grade(taman) #cria o objeto de grade com os atributos de tamanho

grade_numerica.imprimir_grade_prev() #representacao numerica das posicoes da grade

operacao = OperNum(taman, grade_jogo)
random = RandomPosNum(taman, grade_jogo)
tempo = TempoAtual(taman, grade_jogo)


escolha = True

fim = False

endgame = FimJogo(taman, grade_jogo, random)

while True:
    try:
        resp = int(input("Selecione uma jogada: Up (1), Down (2), Left (3), Right (4), Salvar Progresso (5)?\n"))
        if resp == 1:
            operacao.SomaUp()
            random.RandomPos()
            save.salvar_jogo()
            fim = endgame.Fim()
            if random.fim_jogo:  # Verifique se a flag de fim de jogo foi ativada
                remove.apagar_jogo()
                break
        elif resp == 2:
            operacao.SomaDown()
            random.RandomPos()
            save.salvar_jogo()
            fim = endgame.Fim()
            if random.fim_jogo:  # Verifique se a flag de fim de jogo foi ativada
                remove.apagar_jogo()
                break
        elif resp == 3:
            operacao.SomaLeft()
            random.RandomPos()
            save.salvar_jogo()
            fim = endgame.Fim()
            if random.fim_jogo:  # Verifique se a flag de fim de jogo foi ativada
                remove.apagar_jogo()
                break
        elif resp == 4:
            operacao.SomaRight()
            random.RandomPos()
            save.salvar_jogo()
            fim = endgame.Fim()
            if random.fim_jogo:  # Verifique se a flag de fim de jogo foi ativada
                remove.apagar_jogo()
                break
        elif resp == 5:
            save.salvar_jogo()
            resp1 = int(input("Seu jogo foi salvo.\nDeseja sair? 1 - Sim, 2 - Não:\n"))
            if resp1 == 1:
                print("Obrigado por jogar! Desligando...")
                break
            elif resp1 == 2:
                print("Ok, vamos continuar jogando!")
            else:
                print("Escolha uma opção válida:\n")
        else:
            print("Digite uma opção válida:\n")
        
    except ValueError:
        print("Digite uma jogada válida")
    tempo.momento_atual()
    
#anotações 