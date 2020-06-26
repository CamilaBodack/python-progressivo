codigo_usuario = 1
maior_altura = 0
maior_peso = 0


while codigo_usuario != 0:
    codigo_usuario = int(input("Código de usuário:"))
    altura = float(input("Altura:"))
    peso = float(input("Peso:"))
    if altura > maior_altura:
        maior_altura = altura
        cod_cliente_alto = codigo_usuario
    if peso > maior_peso:
        maior_peso = peso
        cod_cliente_pesado = codigo_usuario

else:
    print("Cliente mais alto é:", cod_cliente_alto, "que possui:", maior_altura)
    print("Cliente mais pesado é:", cod_cliente_pesado, "que possui:", maior_peso)
    print("Finalizado.")
