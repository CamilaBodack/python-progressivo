nome  = input("Insira o nome: ")
idade = int(input("Insira a idade: "))
salario = float(input("Insira o salário: "))
sexo = input("Sexo: ")
estado_civil = input("Estado civil:" '\n'
                     "S - Solteiro" '\n'
                     "C - Casado" '\n'
                     "V - Viúva(o)" '\n'
                     "D - Desquitado"'\n')

while len(nome) <= 3 or idade != range(150+1) or salario < 0 or sexo not in 'mf' or estado_civil not in 'scvd':
    print("Preenchimento inválido. Tente novamente.")
    nome = input("Insira o nome: ")
    print(len(nome))
    idade = int(input("Insira a idade: "))
    salario = float(input("Insira o salário: "))
    sexo = input("Sexo: ")
    estado_civil = input("Estado civil:" '\n'
                         "S - Solteiro" '\n'
                         "C - Casado" '\n'
                         "V - Viúva(o)" '\n'
                         "D - Desquitado"'\n')

else:
    print("Usuário cadastrado com sucesso!")