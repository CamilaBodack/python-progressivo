turmas = int(input("Insira a quantidade turmas:"))

alunos = int(input("Insira a quantidade de alunos:"))

turma = alunos/turmas

if turma > 40:
    print("Quantidade de alunos por turma excede o limite")
else:
    print("A quantidade média de alunos por turma é:",turma)
