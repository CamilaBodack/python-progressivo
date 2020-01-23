nome = input("Insira seu nome:")
senha = input("Insira sua senha:")

while nome == senha:
    print("O nome de usuário não pode ser igual a senha. Tente novamente")
    nome = input("Insira seu nome:")
    senha = input("Insira sua senha:")
else:
    print("Usuário logado com sucesso")