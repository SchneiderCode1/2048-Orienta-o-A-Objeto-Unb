import random

import json

class Grade():
    def __init__(self, taman):
        self.taman = taman
        self.total = self.taman ** 2
        
    def CriaListaPos(self):
        return list(range(self.total))

class GradeNum(Grade):
    def __init__(self, taman):
        super().__init__(taman)
        self.grade = self.CriaListaPos()
        
    def imprimir_grade_prev(self):
        for linhas in range(self.taman):
            linha_formatada = " | ".join([f"{str(self.grade[(linhas * self.taman) + i]).rjust(4)}" for i in range(self.taman)])
            print(f"| {linha_formatada} |")
            print("-" * ((8*self.taman) - (self.taman-1)) )
            
class NovoSave():
    def __init__(self):
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
    
    def create_save(self, taman, nome_save):
        try:
            with open("Saves.json", "r") as saves: #abre o json
                SaveGames = json.load(saves)
        except Exception:
            print(f"Erro: {Exception}")
        
        SaveGames[nome_save] = dict(grade = taman, jogo = [0]*(taman**2)) #cria o dicionario interno com lista zerada
        with open("Saves.json", "w") as saves:
            json.dump(SaveGames, saves, indent=4) #adiciona ao json o dicionario com o save
            #print(SaveGames)

class CarregarSave():
    def __init__(self):
        try:
            with open("Saves.json", "r") as saves:
                self.SaveGames = json.load(saves)
        except Exception:
            print(f"Erro: {Exception}")
            
            
    def saves_disponiveis(self):
        self.saves_disp = list(self.SaveGames.keys())
        for save in self.saves_disp:
            index = self.saves_disp.index(save)
            print(f"{save} - {index}")
        return self.saves_disp
    
    def load_save(self, num):
        while True:
            if 0 <= num <= len(self.saves_disp):
                self.nome_save = self.saves_disp[num]
                #print(self.nome_save, "Save")
                break
            else:
                print("Digite um número válido:\n")
            num = int(input("Selecione o número do save que você deseja:.\n"))
            
        try:
            with open("Saves.json", "r") as saves:
                SaveGames = json.load(saves)
        except Exception:
            print(f"Erro: {Exception}")
        
        #print(SaveGames[self.nome_save]["jogo"], "lista jogo")
        self.grade_jogo = SaveGames[self.nome_save]["jogo"]
        
        return self.grade_jogo

    def pegar_nome_save(self):
        return self.nome_save
        

class RemoverSave():
    def __init__(self):
        pass
    
class RandomPosNum(Grade):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman)
        self.grade_jogo = grade_jogo
        self.fim_jogo = False
        
    def RandomPos(self):
        if 0 not in self.grade_jogo:
            self.fim_jogo = True
            print("Não há mais espaço para adicionar números! Fim de jogo!")
            return
        
        while True:
            index = random.randint(0, len(self.grade_jogo)-1)
            if self.grade_jogo[index] == 0: #caso a posição atual seja 0
                self.grade_jogo[index] = random.choices([2,4], weights=[0.75, 0.25], k=1)[0] #adiciona 2 ou 4 aleatoriamente. Probabilidade de 2 = 75% e 4 = 25%
                self.fim_jogo = False
                break
        return self.fim_jogo

class OperNum(RandomPosNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
        self.grade_jogo = grade_jogo
        
    def SomaUp(self): 
        grade_jogo = self.grade_jogo
        for index in range(self.total - self.taman):
            for index in range(self.total - self.taman):
                try:
                    if grade_jogo[index] == 0 or grade_jogo[index] == grade_jogo[index + self.taman]:
                        grade_jogo[index] += grade_jogo[index + self.taman]
                        grade_jogo[index + self.taman] = 0
                        
                    
                except Exception:
                    pass
                    
        return self.grade_jogo
    
    def SomaDown(self):
        grade_jogo = self.grade_jogo
        for index in range(self.total - 1, self.taman - 1, -1):
            for index in range(self.total - 1, self.taman - 1, -1):
                try:
                    if grade_jogo[index] == 0 or grade_jogo[index] == grade_jogo[index - self.taman]:
                        grade_jogo[index] += grade_jogo[index - self.taman]
                        grade_jogo[index - self.taman] = 0
                        
                except Exception:
                    pass
        
        return self.grade_jogo
    
    def SomaLeft(self):
        grade_jogo = self.grade_jogo
        for i in range(self.total): #somar e andar tudo automaticamente até o limite
            for linhas in range(self.taman):
                for index in range(self.taman):    
                    try: 
                        if grade_jogo[index + (linhas*self.taman)] == 0 or grade_jogo[index + (linhas*self.taman)] == grade_jogo[index + (linhas*self.taman) + 1]:
                            if ((index + (linhas*self.taman) + 1) % self.taman) == 0:
                                pass
                            else:
                                grade_jogo[index + (linhas*self.taman)] += grade_jogo[index + (linhas*self.taman) + 1]
                                grade_jogo[index + (linhas*self.taman) + 1] = 0
                                
                    except Exception:
                        pass

        return grade_jogo

    def SomaRight(self): 
        grade_jogo = self.grade_jogo
        for i in range(self.total):
            for linhas in range(self.taman):
                for index in reversed(range(self.taman)):    
                    try:
                        if grade_jogo[index + (linhas*self.taman)] == 0 or grade_jogo[index + (linhas*self.taman)] == grade_jogo[index + (linhas*self.taman) - 1]:
                            if index + (linhas*self.taman) == linhas*self.taman: 
                                pass
                            else:
                                grade_jogo[index + (linhas*self.taman)] += grade_jogo[index + (linhas*self.taman) - 1]
                                grade_jogo[index + (linhas*self.taman) - 1] = 0
                    except Exception:
                        pass
                        
        return grade_jogo

class TempoAtual(OperNum):
    def __init__(self, taman, grade_jogo):
        
        super().__init__(taman, grade_jogo)
    
    def momento_atual(self):
        for linhas in range(self.taman):
            linha_formatada = " | ".join([f"{str(self.grade_jogo[(linhas * self.taman) + i]).rjust(4)}" for i in range(self.taman)])
            print(f"| {linha_formatada} |")
            print("-" * ((8*self.taman) - (self.taman-1)) )
            

class SalvarJogo(TempoAtual):
    def __init__(self, grade_jogo, nome_save, taman = None,):
        if taman is not None:
            super().__init__(taman, grade_jogo)
        else:
            self.grade_jogo = grade_jogo
        self.nome_save = nome_save
    
    def salvar_jogo(self):
        try:
            with open("Saves.json", "r") as saves:
                SaveGames = json.load(saves)
        except Exception:
            print("Erro: {Exception}")
            
        SaveGames[self.nome_save]["jogo"] = self.grade_jogo
        with open("Saves.json", "w") as saves:
            json.dump(SaveGames, saves, indent=4)
        
        
class RemoverJogo(TempoAtual):
    def __init__(self, grade_jogo, nome_save, taman = None,):
        if taman is not None:
            super().__init__(taman, grade_jogo)
        else:
            self.grade_jogo = grade_jogo
        self.nome_save = nome_save
        
    def apagar_jogo(self):
        try:
            print(self.nome_save)
            with open("Saves.json", "r") as saves:
                SaveGames = json.load(saves)
        except Exception:
            print("Erro: {Exception}")
            
        SaveGames.pop(self.nome_save) #remove o save por completo
        with open("Saves.json", "w") as saves:
            json.dump(SaveGames, saves, indent=4)
        #print(SaveGames)    
        
class FimJogo(TempoAtual):
    def __init__(self, taman, grade_jogo, random_pos):
        super().__init__(taman, grade_jogo)
        self.random_pos = random_pos
    def Fim(self):
        if 2048 in self.grade_jogo:
            print("Fim de jogo, seu jogo será apagado!")
            return True
        
        if self.random_pos.fim_jogo:
            print("Não podemos adicionar mais números! Fim de Jogo!\nSeu jogo será apagado.\n")
            return True
    
        