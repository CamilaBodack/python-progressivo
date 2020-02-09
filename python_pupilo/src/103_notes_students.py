q_1 = 'A'
q_2 = 'A'
q_3 = 'A'
q_4 = 'A'
q_5 = 'A'
q_6 = 'A'
q_7 = 'A'
q_8 = 'A'
q_9 = 'A'
q_10 = 'A'

media_notas = 0
pior_nota = 0
pontos = 0
count = 0
nota = 0
total_alunos = 1
total_notas = 0
total_pior = 0
total_melhor = 0

while total_alunos != 0:
    total_alunos = int(input("Deseja inserir aluno ? 1 - Sim/ 2- Não"))
    i = 0
    if total_alunos == 2:
        print("Maior quantidade de alternativas corretas assinaladas:", nota)
        print("Maior quantidade de alternativas erradas assinaladas:", pior_nota)
        print("Total alunos usaram o sistema:", count)
        print("Média notas turma:", total_notas/count)
    else:
        count += 1
        q_1 = input("Alternativa 1:")
        if q_1 == 'A':
            i += 1
            pontos = i
        q_2 = input("Alternativa 2:")
        if q_2 == 'A':
            i += 1
            pontos = i
        q_3 = input("Alternativa 3:")
        if q_3 == 'A':
            i += 1
            pontos = i
        q_4 = input("Alternativa 4:")
        if q_4 == 'A':
            i += 1
            pontos = i
        q_5 = input("Alternativa 5:")
        if q_5 == 'A':
            i += 1
            pontos = i
        q_6 = input("Alternativa 6:")
        if q_6 == 'A':
            i += 1
            pontos = i
        q_7 = input("Alternativa 7:")
        if q_7 == 'A':
            i += 1
            pontos = i
        q_8 = input("Alternativa 8:")
        if q_8 == 'A':
            i += 1
            pontos = i
        q_9 = input("Alternativa 9:")
        if q_9 == 'A':
            i += 1
            pontos = i
        q_10 = input("Alternativa 10:")
        if q_10 == 'A':
            i += 1
            pontos = i
        pior_nota = 10 - i
        nota = i
        total_notas = total_notas + nota
        media_notas = total_notas/count
