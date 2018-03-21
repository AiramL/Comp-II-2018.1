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
