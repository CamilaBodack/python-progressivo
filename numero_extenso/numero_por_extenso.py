# 1. quatros listas
# 2. if para dividir as duas sequencias de dezenas
# 3. adicionar "e" a cada vez que avança uma lista

global numero
global verifica_dezena
global unidade
global dezena
global centena
global milhar
global onde_a_dezenove

numero = int(input("insira o número"))


faixa_dezena = int(numero % 100)
onde_a_dezenove = (faixa_dezena > 10 and faixa_dezena < 20)
unidade = int(numero % 10)
numero = (numero - unidade)/10
dezena = int(numero % 10)
numero = (numero - dezena)/10
centena = int(numero % 10)
numero = (numero - centena)/10
milhar = int(numero % 10)


print("unidade :", unidade, "dezena:", dezena, "centena:", centena,
      "milhar:", milhar)


def verifica_zero(numero):
    if numero == 0:
        return "zero"
    else:
        pass


def verifica_sinal(numero):
    if numero < 0:
        return "menos"
    else:
        pass


def verifica_milhar(milhar):
    mil_ = [None, "um", "dois", "três", "quatro", "cinco", "seis", "sete",
            "oito", "nove"]
    return mil_[milhar] + " mil "


def verifica_centena(centena):
    centenas = [None, "cem", "duzentos", "trezentos", "quatrocentos",
                "quinhentos", "seissentos", "setessentos", "oitocentos",
                "novecentos"]
    return centenas[centena]


def verifica_faixa_dezena(faixa_dezena, dezena):
    if (faixa_dezena > 10 and faixa_dezena < 20):
        posicao = int(faixa_dezena % 10)
        dezena_inicial = [None, "onze", "doze", "treze", "quatorze", "quinze",
                          "dezesseis", "desessete", "dezoito", "dezenove"]
        return dezena_inicial[posicao]
    else:
        dezenas = [None, "dez", "vinte", "trinta", "quarenta", "cinquenta",
                   "sessenta", "setenta", "oitenta", "noventa"]
        return dezenas[dezena]


def verifica_unidade(unidade):
    unidades = [None, "um", "dois", "três", "quatro", "cinco", "seis",
                "sete", "oito", "nove"]
    return unidades[unidade]


if onde_a_dezenove:
    print(verifica_milhar(milhar))
    print(verifica_centena(centena))
    print(verifica_faixa_dezena(faixa_dezena, dezena))

else:
    print(verifica_milhar(milhar))
    print(verifica_centena(centena))
    print(verifica_faixa_dezena(faixa_dezena, dezena))
    print(verifica_unidade(unidade))

