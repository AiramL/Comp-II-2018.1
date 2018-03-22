from Exercicio01 import montarGradeCurricular
from Exercicio02 import inserirDisciplina



def ler_csv(arquivo):
    grade = []
    for linha in arquivo:
        lista = linha.split(',')
        codigo = lista[0]
        nome = lista[1]
        numRequisitos = lista[2]
        requisitos = []
        if numRequisitos != 0:
            for indice in range(3, len(lista)-1):
                requisitos+=[lista[indice]]
        grade = montarGradeCurricular(grade, codigo, nome,  numRequisitos, requisitos)
    arquivo.close()
    return grade

        





    
arquivo = open('C:\\Users\\airam\\Desktop\\Programação\\Python\\Comp II\\aula01\\gradeCurricular.txt','r') # alterar o diretorio do arquivo para o do seu PC


