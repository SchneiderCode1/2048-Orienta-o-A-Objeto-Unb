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
            print(index, f"Posição random: {index}")
            print(self.grade_jogo[index], "A posição contém o número")
            if self.grade_jogo[index] == 0: #caso a posição atual seja 0
                self.grade_jogo[index] = random.choices([2,4], weights=[0.75, 0.25], k=1)[0] #adiciona 2 ou 4 aleatoriamente. Probabilidade de 2 = 75% e 4 = 25%
                return False
    
class OperNum(RandomPosNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
        
    def SomaUp(self): # adiciona um numero aleatório caso uma operação seja realizada
        grade_jogo = self.grade_jogo
        for index in range(self.total - self.taman):
            for index in range(self.total - self.taman):
                try:
                    # print(index, "index")
                    # print(self.taman, self.taman + index, "posicoes debaixo")
                    # print(grade_jogo[index + self.taman], "pos")
                    # print(grade_jogo[index], "elemento")
                    # print(index + self.taman*2, "prox pos ")
                    if grade_jogo[index] == 0 or grade_jogo[index] == grade_jogo[index + self.taman]:
                        #print("Condicao True")
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
                    # print(index, "index")
                    # print(self.taman, self.taman + index, "posicoes debaixo")
                    # print(grade_jogo[index + self.taman], "pos")
                    # print(grade_jogo[index], "elemento")
                    # print(index + self.taman*2, "prox pos ")
                    if grade_jogo[index] == 0 or grade_jogo[index] == grade_jogo[index - self.taman]:
                        #print("Condicao True")
                        grade_jogo[index] += grade_jogo[index - self.taman]
                        grade_jogo[index - self.taman] = 0
                        
                    
                except Exception:
                    print("FIm das linhas")        
        return self.grade_jogo
    
    def SomaLeft(self):  # Movimenta e soma os números para a esquerda
        grade_jogo = self.grade_jogo
        for row in range(self.taman):  # Itera por cada linha
            for col in range(1, self.taman):  # Da segunda coluna até o final
                index = row * self.taman + col
                try:
                    # Mover os números para a esquerda (sem ultrapassar a borda)
                    if grade_jogo[index] == 0:  # Se o elemento for zero, move o próximo número
                        while col > 0 and grade_jogo[index] == 0:  # Move os números para a esquerda
                            index -= 1
                            col -= 1
                    if grade_jogo[index - 1] == 0 or grade_jogo[index - 1] == grade_jogo[index]:
                        grade_jogo[index - 1] += grade_jogo[index]
                        grade_jogo[index] = 0
                except Exception:
                    pass
        return self.grade_jogo

    def SomaRight(self):  # Movimenta e soma os números para a direita
        grade_jogo = self.grade_jogo
        for row in range(self.taman):  # Itera por cada linha
            for col in range(self.taman - 2, -1, -1):  # Da penúltima coluna até a primeira
                index = row * self.taman + col
                try:
                    # Mover os números para a direita (sem ultrapassar a borda)
                    if grade_jogo[index] == 0:  # Se o elemento for zero, move o próximo número
                        while col < self.taman - 1 and grade_jogo[index] == 0:  # Move os números para a direita
                            index += 1
                            col += 1
                    if grade_jogo[index + 1] == 0 or grade_jogo[index + 1] == grade_jogo[index]:
                        grade_jogo[index + 1] += grade_jogo[index]
                        grade_jogo[index] = 0
                except Exception:
                    pass
        return self.grade_jogo
    
class TempoAtual(OperNum):
    def __init__(self, taman, grade_jogo):
        super().__init__(taman, grade_jogo)
    
    def momento_atual(self):
        print(self.grade_jogo, "Momento atual lista")
        for linhas in range(self.taman):
            linha_formatada = " | ".join([f"{str(self.grade_jogo[(linhas * self.taman) + i]).rjust(4)}" for i in range(self.taman)])
            print(f"| {linha_formatada} |")
            print("-" * ((8*self.taman) - (self.taman-1)) )
            
            

