import random
from random import choices
from colorama import Fore, Style, init

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
        contador = 0
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
        index = random.randint(0, len(self.grade_jogo)-1)
        if self.grade_jogo[index] == 0: #caso a posição atual seja 0
            self.grade_jogo[index] = random.choices([2,4], weights=[0.75, 0.25], k=1)[0] #adiciona 2 ou 4 aleatoriamente. Probabilidade de 2 = 75% e 4 = 25%
        
    
class OperNum(RandomPosNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
        # adiciona um numero aleatório caso uma operação seja realizada
    
    def SomaUp(self):
        self.RandomPos()
    
class TempoAtual(OperNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
    
    def momento_atual(self):
        print(self.grade_jogo, "Momento atual lista")
            

