from package import *
import colorama

taman = int(input("Qual é o tamanho da grade desejada? Ex:. 5 -> 5x5\n"))

grade_numerica= GradeNum(taman) #cria o objeto de grade Numerica

grade = Grade(taman) #cria o objeto de grade com os atributos de tamanho

grade_jogo = GradeJogo(taman) #representação real da grade do jogo, zera cada posição
grade_jogo.Tranform0() #zera as posições

grade_numerica.imprimir_grade_prev() #representacao numerica das posicoes da grade

operacao = OperNum(taman, grade_jogo.grade_jogo)

tempo = TempoAtual(taman, grade_jogo.grade_jogo)


for i in range(5):
 operacao.SomaUp()
 tempo.momento_atual()
    
    
#anotações 