''' crie um programa em python que pela a nota do aluno, que deve ser um float entre 0 e 10
    <= 6: f
    6-7: d
    7-8: c
    8-9: b
    9-10: a
    '''
note = float(input("Insira a nota"))

if note <=6.0:
    print("F")
elif note <=7.0:
    print("D")
elif note <= 8.0:
    print("C")
elif note <= 9.0:
    print("B")
else:
    print("A")
    
