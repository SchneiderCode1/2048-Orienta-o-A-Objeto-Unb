import random

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
    
    def RandomPos(self):
        pos_index = random.randint(0, len(self.lista_pos)-1)
        pos_num = True
        
        while pos_num == True:
            try:
                if self.lista_pos[pos_index] == 0:
                    self.lista_pos[pos_index] += 2
                    pos_num = False
                else:
                    pos_index = random.randint(0, len(self.lista_pos)-1)
            except Exception:
                pos_num = True
    
    
class OperNum(RandomPosNum):
    def __init__(self):
        super().__init__()
        
    def SomaUp(self):
        for i in range(0, len(self.lista_pos)-1):
            try:
                
            except IndexError:
                pass 
            
        return self.lista_pos
    


class ProxJogada(OperNum):
    def __init__(self):
        super().__init__()
    
    def PrintBoard(self):
        print(f"""
            ---------------------
            |  {self.lista_pos[0]}  |  {self.lista_pos[1]}  |  {self.lista_pos[2]}  |  {self.lista_pos[3]}  |  {self.lista_pos[4]}  |
            ---------------------
            |  {self.lista_pos[5]}  |  {self.lista_pos[6]}  |  {self.lista_pos[7]}  |  {self.lista_pos[8]}  |  {self.lista_pos[9]}  |
            ---------------------
            |  {self.lista_pos[10]}  |  {self.lista_pos[11]}  |  {self.lista_pos[12]}  |  {self.lista_pos[13]}  |  {self.lista_pos[14]}  |
            ---------------------
            |  {self.lista_pos[15]}  |  {self.lista_pos[16]}  |  {self.lista_pos[17]}  |  {self.lista_pos[18]}  |  {self.lista_pos[19]}  |
            ---------------------
            |  {self.lista_pos[20]}  |  {self.lista_pos[21]}  |  {self.lista_pos[22]}  |  {self.lista_pos[23]}  |  {self.lista_pos[24]}  | 
            ---------------------
            """)

class FimDeJogo(ProxJogada):
    def __init__(self):
        super().__init__()
    
    def Fim(self, endGame):
        for pos in self.lista_pos:
            if pos == 2048:
                print("Fim de Jogo")
