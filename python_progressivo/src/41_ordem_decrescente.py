# comparar e trocar os valores das variáveis duas a duas.
# no 1° igual atribuir a variavel auxiliar o maior valor
# no 2° igual atribui o segundo maior valor a ela para nao perde-lo.
# atribui o valor maior a segunda variavel para que ela fique com o maior valor e
# seja comparada no próximo bloco.

a = int(input("primeiro"))
b = int(input("segundo"))
c = int(input("terceiro"))

m = 0

if c > b:
    m = c
    c = b
    b = m

if b > a:
    m = b
    b = a
    a = m

if c > b:
    m = c
    c = b
    b = m

print("ordem decrescente :", a, "-", b, "-", c)

    

    
