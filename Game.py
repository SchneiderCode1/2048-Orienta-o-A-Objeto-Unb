from package import *
import json
import time 
try:
    with open("Saves.json", "r") as saves: #caso exista algo no json
        json_save = json.load(saves)
        print(json_save, "Coisas dentro de Saves")
            
except Exception: #caso não exista nada no json
    print(Exception, "Exception")
    with open("Saves.json", "w") as saves:
        SaveGames = dict()
        print(SaveGames,"Dicionario")
        json.dump(SaveGames, saves)

entrada = int(input("Bem Vindo!\nEsse é um jogo chamado 2048.\nSelecione uma opção para continuar:\n1 - Novo Jogo\n2 - Carregar jogo salvo\n3 - Regras\n4 - Apagar jogos salvos\n\n"))
escolha = True
while True:
    if entrada == 1: # Novo Jogo #finaliza a escolha e passa para o jogo
        print("Vamos iniciar o jogo!")
        nome_save = str(input("Qual será o nome do seu Save? Ex:. save_1 :\n"))
        taman = int(input("Qual é será1 o tamanho da sua grade de jogo? Ex:. 5 -> 5x5 : \n"))
        try:
            with open("Saves.json", "r") as saves: #abre o json
                SaveGames = json.load(saves)
        except Exception:
            print(f"Erro: {Exception}")
        
        SaveGames[nome_save] = dict(grade = taman, jogo = '...') #cria o dicionario interno 
        with open("Saves.json", "w") as saves:
            json.dump(SaveGames, saves, indent=4) #adiciona ao json o dicionario com o save
            print(SaveGames)
            break
    elif entrada == 2:#Carregar Jogo
        try:
            with open("Saves.json", "r") as saves:
                SaveGames = json.load(saves)
        except Exception:
            print(f"Erro: {Exception}")

        save_names = list(SaveGames.keys())
        for save in save_names:
            index = save_names.index(save)
            print(f"{save} - {index}")
        
        while True:
            save_index = int(input("Selecione o número do Save:\n"))
            if 1 <= save_index <= len(save_names):
                nome_save = save_names[save_index]
                print(nome_save, "Save")
                break
            else:
                print("Digite um número válido:\n")
        break
    elif entrada == 3:
        entrada = 0
        print("Regras:\nO objetivo do jogo é chegar ao número 2048.\nCada movimento leva todos os elementos da grade até a borda e soma os números iguais, Ex:. 2 + 2 + 2 + 2 = 4 + 4 = 8.\nCada movimento adiciona um número 2 ou 4 em uma posição vazia aleatória.\n")
    
    elif entrada == 4: # Apagar jogos salvos
        entrada = 0
        try:
            with open("Saves.json", "r") as saves:
                SaveGames = json.load(saves) #Resetar todos os saves
        except Exception:
            print(f"Erro: {Exception}")
        SaveGames = {}
        with open("Saves.json", "w") as saves:
            json.dump(SaveGames, saves, indent=4)
    elif entrada == 0:
        entrada = int(input("Bem Vindo!\nEsse é um jogo chamado 2048.\nSelecione uma opção para continuar:\n1 - Novo Jogo\n2 - Carregar jogo salvo\n3 - Regras\n4 - Apagar jogos salvos\n\n"))
        



grade_numerica= GradeNum(taman) #cria o objeto de grade Numerica

grade = Grade(taman) #cria o objeto de grade com os atributos de tamanho

grade_jogo = GradeJogo(taman, nome_save)#representação real da grade do jogo, zera cada posição

grade_jogo.Tranform0() #zera as posições

grade_numerica.imprimir_grade_prev() #representacao numerica das posicoes da grade

operacao = OperNum(taman, grade_jogo.grade_jogo)

random = RandomPosNum(taman, grade_jogo.grade_jogo)

tempo = TempoAtual(taman, grade_jogo.grade_jogo)

save = SalvarJogo(taman, grade_jogo.grade_jogo)

escolha = True
while escolha:
    resp = int(input("Selecione uma jogada: Up (1), Down (2), Left (3), Right (4), Salvar Progresso (5)?\n"))
    if resp == 1:
        operacao.SomaUp()
        random.RandomPos()
    elif resp == 2:
        operacao.SomaDown()
        random.RandomPos()
    elif resp == 3:
        operacao.SomaLeft()
        random.RandomPos()
    elif resp == 4:
        operacao.SomaRight()
        random.RandomPos()
    elif resp == 5:
        save.salvar_jogo(nome_save)
        resp = int(input("Seu jogo foi salvo. Deseja sair? 1 - Sim, 2 - Não:\n"))
        if resp == 1:
            escolha = False
        elif resp == 2:
            escolha = True
        else:
            print("Escolha uma opção válida:\n")
    else:
        print("Digite um número válido")
    tempo.momento_atual()
    
#anotações 




