def montarGradeCurricular(gradeCurricular, codigo, nome, numRequisitos, requisitos):
    if gradeCurricular != []:
        for cont in range(len(gradeCurricular)):
            dicionario = gradeCurricular[cont]
            dicionario.values
            if codigo in dict.values(dicionario):
                return gradeCurricular
    nova_disciplina = {"codigo": codigo, "nome": nome, "numRequisitos": numRequisitos, "requisitos": requisitos}
    gradeCurricular+=[nova_disciplina]
    return gradeCurricular

def inserirDisciplina(gradeCurricular):
    nome = raw_input("\nQual o nome da disciplina?\n")
    codigo = raw_input("\nQual o codigo da disciplina?\n")
    numRequisitos = int(raw_input("\nQual o numero de requisitos da disciplina?\n"))
    if numRequisitos != 0:
        requisito = raw_input("\nQuais são os codigos das disciplinas que são pre-requisitos?\n")

    else:
        requisito = []
    montarGradeCurricular(gradeCurricular, codigo, nome, numRequisitos, requisito)
    return gradeCurricular
