
notas_alunos = {}

while True:
    options = int(input("0. Sair \n"
                        "1. Exibir lista de alunos com suas notas (cada aluno tem uma nota) \n"
                        "2. Inserir aluno e nota \n"
                        "3. Alterar a nota de um aluno \n"
                        "4. Consultar nota de um aluno específico \n"
                        "5. Apagar um aluno da lista \n"
                        "6. Dar a média da turma"))
    if options == 0:
        print("Finalizando...")
    elif options == 1:
        print(notas_alunos.items())
    elif options == 2:
        nome = input("Nome aluno:")
        nota = float(input("Nota:"))
        if notas_alunos.get(nome):
            print("Nome já existe")
        else:
            notas_alunos[nome] = nota
    elif options == 3:
        nome = input("Nome aluno:")
        nota = float(input("Nota:"))
        if nome in notas_alunos.keys():
            notas_alunos[nome] = nota
        else:
            print("Aluno inexistente")
    elif options == 4:
        nome = input("Nome aluno:")
        if nome in notas_alunos.keys():
            print(notas_alunos[nome].value())
        else:
            print("Alunos inexistente")
    elif options == 5:
        nome = input("Nome aluno:")
        if nome in notas_alunos.keys():
            notas_alunos.pop(nome)
        else:
            print("Alunos inexistente")
    elif options == 6:
        soma = 0
        for count in notas_alunos.values():
            soma += count
        media = notas_alunos.values()/soma
        print(media)
