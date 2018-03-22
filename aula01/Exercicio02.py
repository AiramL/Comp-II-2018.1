from Exercicio01 import montarGradeCurricular

def inserirDisciplina(gradeCurricular):
    nome = raw_input("\n Qual o nome da disciplina? \n")
    codigo = raw_input("\n Qual o codigo da disciplina? \n")
    numRequisitos = int(raw_input("\n Qual o numero de requisitos da disciplina? \n"))
    if numRequisitos != 0:
        requisitos = []
        for contador in range(numRequisitos):
            requisitos +=  [raw_input("\n Qual eh o codigo da disciplina que eh o " + str(contador+1) + " pre-requisito?\n")]
    else:
        requisitos = []
    montarGradeCurricular(gradeCurricular, codigo, nome, numRequisitos, requisitos)
    return gradeCurricular
