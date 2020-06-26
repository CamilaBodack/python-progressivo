def menu():
    options = 7
    while options:
        options = int(input("0. Sair \n"
                            "1. Exibir lista de alunos com suas notas (cada aluno tem uma nota) \n"
                            "2. Inserir aluno e nota \n"
                            "3. Alterar a nota de um aluno \n"
                            "4. Consultar nota de um aluno específico \n"
                            "5. Apagar um aluno da lista \n"
                            "6. Dar a média da turma \n"
                            "7. Exibir menu"))

        if options == 0:
            finalizar()
        elif options == 1:
            exibir_alunos()
        elif options == 2:
            inserir_nota_aluno()
        elif options == 3:
            alterar_nota_aluno()
        elif options == 4:
            consultar_nota_aluno()
        elif options == 5:
            apagar_aluno()
        elif options == 6:
            media_alunos()


def finalizar():
    print("Finalizando...")


def exibir_alunos():
    print(notas_alunos.items())


def inserir_nota_aluno():
    nome = input("Nome aluno:")
    nota = float(input("Nota:"))
    if notas_alunos.get(nome):
        print("Nome já existe")
    else:
        notas_alunos[nome] = nota


def alterar_nota_aluno():
    nome = input("Nome aluno:")
    nota = float(input("Nota:"))
    if nome in notas_alunos.keys():
        notas_alunos[nome] = nota
    else:
        print("Aluno inexistente")


def consultar_nota_aluno():
    nome = input("Nome aluno:")
    if notas_alunos.get(nome):
        print("Aluno:", nome, ":", notas_alunos[nome])
    else:
        print("Alunos inexistente")


def apagar_aluno():
    nome = input("Nome aluno:")
    if nome in notas_alunos.keys():
        notas_alunos.pop(nome)
    else:
        print("Alunos inexistente")


def media_alunos():
    soma = 0
    for count in notas_alunos.values():
        soma += count
    print("Média da turma:", soma/len(notas_alunos))


notas_alunos = {}
menu()
