note_1 = float(input("Primeira prova"))
note_2 = float(input("Segundo prova"))

media = (note_1 + note_2)/2

if media >= 9.0 and media <= 10.0:
    print("Notas:",note_1, note_2)
    print("Média:",media)
    print("A")
    print("Aprovado")

elif media >= 7.5 and media < 9.0:
    print("Notas:",note_1, note_2)
    print("Média:",media)
    print("B")
    print("Aprovado")

elif media >= 6.0 and media < 7.5:
    print("Notas:",note_1, note_2)
    print("Média:",media)
    print("C")
    print("Aprovado")

elif media >= 4.0 and media < 6.0:
    print("Notas:",note_1, note_2)
    print("Média:",media)
    print("D")
    print("Reprovado")

elif media >= 0 and media < 4.0:
    print("Notas:",note_1, note_2)
    print("Média:",media)
    print("E")
    print("Reprovado")
    
