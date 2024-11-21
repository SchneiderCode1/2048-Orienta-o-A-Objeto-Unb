import random
from colorama import Fore, Style, init

class Grade():
    def __init__(self):
        self.pos01, self.pos02, self.pos03, self.pos04, self.pos05 = 0, 0, 0, 0, 0
        self.pos11, self.pos12, self.pos13, self.pos14, self.pos15 = 0, 0, 0, 0, 0
        self.pos21, self.pos22, self.pos23, self.pos24, self.pos25 = 0, 0, 0, 0, 0
        self.pos31, self.pos32, self.pos33, self.pos34, self.pos35 = 0, 0, 0, 0, 0
        self.pos41, self.pos42, self.pos43, self.pos44, self.pos45 = 0, 0, 0, 0, 0
        
    def CriaListaPos(self):
        return [
            self.pos01, self.pos02, self.pos03, self.pos04, self.pos05,
            self.pos11, self.pos12, self.pos13, self.pos14, self.pos15,
            self.pos21, self.pos22, self.pos23, self.pos24, self.pos25,
            self.pos31, self.pos32, self.pos33, self.pos34, self.pos35,
            self.pos41, self.pos42, self.pos43, self.pos44, self.pos45,
        ]

class RandomPosNum(Grade):
    def __init__(self):
        super().__init__()
        self.lista_pos = self.CriaListaPos()
        self.endGame = False
    
    def RandomPos(self):
        pos_index = random.randint(0, len(self.lista_pos)-1)
        pos_num = True
        cont = 0
        while pos_num == True:
            if cont >=25:
                self.endGame = True
                print("Game over! Não é possível adicionar mais nenhum número!")
                return
            
            try:
                if self.lista_pos[pos_index] == 0:
                    self.lista_pos[pos_index] += 2
                    pos_num = False
                else:
                    pos_index = random.randint(0, len(self.lista_pos)-1)
                    cont += 1
            except Exception:
                pos_num = True
    
    
class OperNum(RandomPosNum):
    def __init__(self):
        super().__init__()
        
    def SomaUp(self):
        for z in range(4):
            for i in range(5, 10):
                if self.lista_pos[i-5] == 0 or self.lista_pos[i-5] == self.lista_pos[i]: 
                    self.lista_pos[i-5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
                    
            for i in range(10, 15):
                if self.lista_pos[i-5] == 0 or self.lista_pos[i-5] == self.lista_pos[i]: 
                    self.lista_pos[i-5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
                    
            for i in range(15, 20):
                if self.lista_pos[i-5] == 0 or self.lista_pos[i-5] == self.lista_pos[i]: 
                    self.lista_pos[i-5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
                    
            for i in range(20, 25): #Linha 5
                        #linha 5 -> 4, [i-5] = Linha 4
                        if self.lista_pos[i-5] == 0 or self.lista_pos[i-5] == self.lista_pos[i]:
                            self.lista_pos[i-5] += self.lista_pos[i] 
                            self.lista_pos[i] = 0
                
        return self.lista_pos
    
    def SomaDown(self):
        for z in range(4):
            for i in range(15, 20):
                if self.lista_pos[i+5] == 0 or self.lista_pos[i+5] == self.lista_pos[i]:
                    self.lista_pos[i+5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
                
            for i in range(10, 15):
                if self.lista_pos[i+5] == 0 or self.lista_pos[i+5] == self.lista_pos[i]:
                    self.lista_pos[i+5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
            
            for i in range(5, 10):
                if self.lista_pos[i+5] == 0 or self.lista_pos[i+5] == self.lista_pos[i]:
                    self.lista_pos[i+5] += self.lista_pos[i]
                    self.lista_pos[i] = 0
            
            for i in range(0, 5):
                if self.lista_pos[i+5] == 0 or self.lista_pos[i+5] == self.lista_pos[i]:
                    self.lista_pos[i+5] += self.lista_pos[i]
                    self.lista_pos[i] = 0        
        return self.lista_pos
    
    def SomaLeft(self):
        for z in range(4):
            for i in range(1, 22, 5):
                if self.lista_pos[i-1] == 0 or self.lista_pos[i-1] == self.lista_pos[i]:
                    self.lista_pos[i-1] += self.lista_pos[i]
                    self.lista_pos[i] = 0

            for i in range(2, 23, 5):
                if self.lista_pos[i-1] == 0 or self.lista_pos[i-1] == self.lista_pos[i]:
                    self.lista_pos[i-1] += self.lista_pos[i]
                    self.lista_pos[i] = 0    
                    
            for i in range(3, 24, 5):
                if self.lista_pos[i-1] == 0 or self.lista_pos[i-1] == self.lista_pos[i]:
                    self.lista_pos[i-1] += self.lista_pos[i]
                    self.lista_pos[i] = 0    
                    
            for i in range(4, 25, 5):
                if self.lista_pos[i-1] == 0 or self.lista_pos[i-1] == self.lista_pos[i]:
                    self.lista_pos[i-1] += self.lista_pos[i]
                    self.lista_pos[i] = 0  
        
        return self.lista_pos
    
    def SomaRight(self):
        for z in range(4):
            for i in range(3, 24, 5):
                if self.lista_pos[i+1] == 0 or self.lista_pos[i+1] == self.lista_pos[i]:
                    self.lista_pos[i+1] += self.lista_pos[i]
                    self.lista_pos[i] = 0
                    
            for i in range(2, 23, 5):
                if self.lista_pos[i+1] == 0 or self.lista_pos[i+1] == self.lista_pos[i]:
                    self.lista_pos[i+1] += self.lista_pos[i]
                    self.lista_pos[i] = 0  

            for i in range(1, 22, 5):
                if self.lista_pos[i+1] == 0 or self.lista_pos[i+1] == self.lista_pos[i]:
                    self.lista_pos[i+1] += self.lista_pos[i]
                    self.lista_pos[i] = 0   

            for i in range(0, 21, 5):
                if self.lista_pos[i+1] == 0 or self.lista_pos[i+1] == self.lista_pos[i]:
                    self.lista_pos[i+1] += self.lista_pos[i]
                    self.lista_pos[i] = 0       
        return self.lista_pos
    
class ProxJogada(OperNum):
    def __init__(self):
        super().__init__()
    
    def vermelho(self, texto):
        return f"{Fore.RED}{texto}{Fore.RESET}"  # Usa a cor vermelha para 0.

    def verde(self, texto):
        return f"\033[38;2;154;255;0m{texto}\033[0m"  # Usa a cor verde para outros números.

    def formatar_numero(self, numero):
        num_formatado = f"{numero}".rjust(4)  # Ajuste para garantir que o número ocupe 4 espaços.
        return self.vermelho(num_formatado) if numero == 0 else self.verde(num_formatado)
    
    def PrintBoard(self):
        print(f"""
        -----------------------------------------------
        |  {self.formatar_numero(self.lista_pos[0])}  |  {self.formatar_numero(self.lista_pos[1])}  |  {self.formatar_numero(self.lista_pos[2])}  |  {self.formatar_numero(self.lista_pos[3])}  |  {self.formatar_numero(self.lista_pos[4])}  |
        -----------------------------------------------
        |  {self.formatar_numero(self.lista_pos[5])}  |  {self.formatar_numero(self.lista_pos[6])}  |  {self.formatar_numero(self.lista_pos[7])}  |  {self.formatar_numero(self.lista_pos[8])}  |  {self.formatar_numero(self.lista_pos[9])}  |
        -----------------------------------------------
        |  {self.formatar_numero(self.lista_pos[10])}  |  {self.formatar_numero(self.lista_pos[11])}  |  {self.formatar_numero(self.lista_pos[12])}  |  {self.formatar_numero(self.lista_pos[13])}  |  {self.formatar_numero(self.lista_pos[14])}  |
        -----------------------------------------------
        |  {self.formatar_numero(self.lista_pos[15])}  |  {self.formatar_numero(self.lista_pos[16])}  |  {self.formatar_numero(self.lista_pos[17])}  |  {self.formatar_numero(self.lista_pos[18])}  |  {self.formatar_numero(self.lista_pos[19])}  |
        -----------------------------------------------
        |  {self.formatar_numero(self.lista_pos[20])}  |  {self.formatar_numero(self.lista_pos[21])}  |  {self.formatar_numero(self.lista_pos[22])}  |  {self.formatar_numero(self.lista_pos[23])}  |  {self.formatar_numero(self.lista_pos[24])}  |
        -----------------------------------------------
    """)
    
    def format_number(self, num):
        return f"{num:4}"


class FimDeJogo(ProxJogada):
    def __init__(self):
        super().__init__()
        self.endGame = False
    
    def Fim(self):
        cont = 0
        for pos in self.lista_pos:
            if pos == 2048:
                self.endGame == True
                break
