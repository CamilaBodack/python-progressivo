note_1 = float(input("Primeira nota"))
note_2 = float(input("Segunda nota"))

media = (note_1 + note_2)/2

if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
    


