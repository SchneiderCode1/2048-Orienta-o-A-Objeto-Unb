import random

import json
import time

class SaveGame():
    def __init__(self):
        pass
    
    def cria_jogo(self, nome, taman):
        self.jogos = jogos
        jogos = dict(saves = dict(nome = nome, grade = taman))
        return jogos


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
            
class GradeJogo(Grade):
    def __init__(self, taman):
        super().__init__(taman)
        
        self.grade_jogo = self.CriaListaPos()
        
    def Tranform0(self): # zerar posicoe
        self.grade_jogo = [0] * self.total
        return self.grade_jogo
        # for i in range(len(self.grade_jogo)):
        #     self.grade_jogo[i] = 0
        # print(self.grade_jogo)

class RandomPosNum(GradeJogo):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman)
        self.grade_jogo = grade_jogo
    
    def RandomPos(self):
        while True:
            index = random.randint(0, len(self.grade_jogo)-1)
            if self.grade_jogo[index] == 0: #caso a posição atual seja 0
                self.grade_jogo[index] = random.choices([2,4], weights=[0.75, 0.25], k=1)[0] #adiciona 2 ou 4 aleatoriamente. Probabilidade de 2 = 75% e 4 = 25%
                return False
    
class OperNum(RandomPosNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
        
    def SomaUp(self): 
        grade_jogo = self.grade_jogo
        for index in range(self.total - self.taman):
            for index in range(self.total - self.taman):
                try:
                    if grade_jogo[index] == 0 or grade_jogo[index] == grade_jogo[index + self.taman]:
                        grade_jogo[index] += grade_jogo[index + self.taman]
                        grade_jogo[index + self.taman] = 0
                        
                    
                except Exception:
                    print("FIm das linhas")
                    
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
                    print("FIm das linhas") 
        
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
                        print("Fim das linhas", Exception)

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
                        print("Fim das linhas", Exception)
                        
        return grade_jogo

class TempoAtual(OperNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
    
    def momento_atual(self):
        print(self.grade_jogo, "Momento atual lista")
        for linhas in range(self.taman):
            linha_formatada = " | ".join([f"{str(self.grade_jogo[(linhas * self.taman) + i]).rjust(4)}" for i in range(self.taman)])
            print(f"| {linha_formatada} |")
            print("-" * ((8*self.taman) - (self.taman-1)) )
            

class SalvarJogo():
    def __init__(self):
        pass
    
    def salvar_jogo(self):
        