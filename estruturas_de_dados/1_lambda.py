'''
Funcoes anonimas
'''


def potencia(x):
    return lambda x: x**2


def fatorial(numero):
    return lambda numero: numero * fatorial(numero-1) if numero > 1 else 1
