from Exercicio01 import montarGradeCurricular
from Exercicio02 import inserirDisciplina

arquivo = open('C:\\Users\\airam\\Desktop\\Programação\\Python\\Comp II\\aula01\\gradeCurricular.txt','r') # alterar o diretorio do arquivo para o do seu PC


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


    
def excluirDisciplina(gradeCurricular):
    controle = False
    codigo = raw_input("Qual o codigo da disciplina que voce deseja excluir? ")
    for cont in range(len(gradeCurricular)):
        dicionario = gradeCurricular[cont]
        if codigo in dict.values(dicionario):
            controle = True
            del gradeCurricular[cont]
    if controle == False:
        print "Disciplina nao cadastrada ou inexistente"
        return
    print "Disciplina excluida"
    return


def alterarDisciplina(gradeCurricular):
    controle = False
    codigo = raw_input("Qual o codigo da disciplina que voce deseja ? ")
    for cont in range(len(gradeCurricular)):
        dicionario = gradeCurricular[cont]
        if codigo in dict.values(dicionario):
            print dicionario
            controle = True
            print "Nome da disciplina: " + dicionario['nome']
            r_nome = raw_input("Deseja alterar o nome da disciplina? (Digite 1 para sim) \n")
            if r_nome == '1':
                dicionario['nome'] = raw_input('Qual o novo nome? \n')
            print "Codigo: " + dicionario['codigo']
            r_codigo = raw_input("Deseja alterar o codigo da disciplina? (Digite 1 para sim) \n")
            if r_codigo == '1':
                dicionario['codigo'] = raw_input('Qual o novo codigo? \n')
            print "Numero de requisitos: " + str(dicionario['numRequisitos'])
            print "Pre-requisitos: "
            for loop in range(len(dicionario['requisitos'])):
                 print '\n'+ dicionario['requisitos'][loop]
            r_nu = raw_input("Deseja alterar o numero de requisitos da disciplina? (Digite 1 para sim) \n")
            numrequisitos = 0
            if r_nu == '1':
                numrequisitos = raw_input('Qual o novo numero de requisitos? \n')
                dicionario['numRequisitos'] = numrequisitos
            if numrequisitos != 0:
                requisitos = []
                for c in range(int(numrequisitos)):
                    Requisitos +=  [raw_input("Qual eh o codigo da disciplina que eh o " + str(c+1) + " pre-requisito?\n")]
                dicionario['requisitos'] = Requisitos
    if controle == False:
        print "Disciplina nao cadastrada ou inexistente"
        return 
    print "Disciplina alterada com sucesso"
    return

def mostrarGradeCurricular(gradeCurricular):
    for cont in range(len(gradeCurricular)):
        dicionario = gradeCurricular[cont]
        codigo = dict.values(dicionario)[0]
        if codigo in dict.values(dicionario):
            controle = True
            print "\nDisciplina: " + dicionario['codigo']
            print "Nome: " + dicionario['nome']
            print "Quantidade de pre-requisitos: " + str(dicionario['numRequisitos'])
            print "Pre-requisitos: "+ str(dicionario['requisitos'])+'\n'
            
        

def mostrarDisciplina(gradeCurricular):
    controle = False
    codigo = raw_input("Qual o codigo da disciplina que deseja ver? ")
    for cont in range(len(gradeCurricular)):
        dicionario = gradeCurricular[cont]
        dicionario.values
        if codigo in dict.values(dicionario):
            controle = True
            print "\nDisciplina: " + dicionario['codigo']
            print "Nome: " + dicionario['nome']
            print "Quantidade de pre-requisitos: " + str(dicionario['numRequisitos'])
            print "Pre-requisitos: " + str(dicionario['requisitos'])+'\n'
            return 
    if controle == False:
        print "Disciplina nao cadastrada ou inexistente"
        return

def mostrarDisciplinasPresas(gradeCurricular):
    controlador = True
    codigo = raw_input('Qual o codigo da disciplina que deseja ver? ')
    for dicionario in gradeCurricular:
        if codigo in dicionario['requisitos']:
            controle = False
            print "\nDisciplina: " + dicionario['codigo']
            print "Nome: " + dicionario['nome']
            print "Quantidade de pre-requisitos: " + str(dicionario['numRequisitos'])
            print "Pre-requisitos: " + str(dicionario['requisitos'])+'\n'            
    if controlador == True:
        print 'Disciplina nao cadastrada ou inexistente'
        return
    return 

def mostrarDisciplinasFaltam(disciplinasCursadas,gradeCurricular):
    gradeCurricular = gradeCurricular
    for codigo in disciplinasCursadas:
        for controlador in gradeCurricular:
            if codigo in dict.values(controlador):
                gradeCurricular.remove(controlador)
    mostrarGradeCurricular(gradeCurricular)
    return
    

def disciplinasDisponiveis():
    pass
