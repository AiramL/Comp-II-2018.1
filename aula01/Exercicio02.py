from Exercicio01 import montarGradeCurricular

def inserirDisciplina(gradeCurricular):
    nome = raw_input("\nQual o nome da disciplina?\n")
    codigo = raw_input("\nQual o codigo da disciplina?\n")
    numRequisitos = int(raw_input("\nQual o numero de requisitos da disciplina?\n"))
    if numRequisitos != 0:
        requisitos = []
        for contador in range(numRequisitos):
            requisitos +=  [raw_input("\nQual eh o codigo da disciplina que eh o " + str(contador+1) + "º pre-requisito?\n")]

    else:
        requisitos = []
    montarGradeCurricular(gradeCurricular, codigo, nome, numRequisitos, requisito)
    return gradeCurricular
