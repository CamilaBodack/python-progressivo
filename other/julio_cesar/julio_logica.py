#!usr/bin/python3

criptografado = (
    'mx mw e qmvegpi xlex gyvmswmxc wyvzmziw jsvqep ihygexmsr. epfivx imrwximr'
    )

sem_espaco = criptografado.replace(" ", "")
sem_ponto_nem_espaco = sem_espaco.replace(".", "")
casas = 4

todos_chars = []
decrypt_char = []
final_char = []

for char in sem_ponto_nem_espaco:
    if char.isalpha():
        chars = ord(char)
        todos_chars.append(chars)
    else:
        pass
print('--- todos chars', todos_chars)

for ascii_char in todos_chars:
    ascii_char -= casas
    decrypt_char.append(ascii_char)
print('---decrypt', decrypt_char)

for chars in decrypt_char:
    if chars >= 0:
        letter = chr(chars)
        final_char.append(letter)
print('---finalchar', final_char)
