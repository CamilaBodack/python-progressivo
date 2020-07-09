#!usr/bin/python3
'''
List comprehension é uma forma de criar listas com código mais compacto.
'''

'''
Ao invés de fazer: for num in range(10):
                        if num % 2 == 0:
                            print(pares)

Com list compreehension:
'''


def pares(num):
    pares = [num for num in range(10) if (num % 2 == 0)]
    return pares


def impar(num):
    impar = [num for num in range(10) if (num % 2 != 0)]
    return impar


def impar_cem(num):
    impar_ate_cem = [numero for numero in range(101) if (numero % 2 != 0)]
    return impar_cem
