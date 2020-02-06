cod_maior_aluno = 0
cod_menor_aluno = 0
maior_altura = 0
menor_altura = 2

for i in range(10):
    cod_aluno = int(input("Código aluno:"))
    altura_aluno = float(input("Altura:"))
    if altura_aluno > maior_altura:
        maior_altura = altura_aluno
        cod_maior_aluno = cod_aluno
    if altura_aluno < menor_altura:
        menor_altura = altura_aluno
        cod_menor_aluno = cod_aluno

print("Código aluno mais alto:", cod_maior_aluno, "altura:", maior_altura)
print("Código aluno mais baixo:", cod_menor_aluno, "altura:", menor_altura)
