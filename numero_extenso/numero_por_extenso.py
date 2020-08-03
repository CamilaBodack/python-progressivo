
# 1. quatros listas
# 2. if para dividir as duas sequencias de dezenas
# 3. adicionar "e" a cada vez que avança uma lista

global numero
global verifica_dezena
global unidade
global dezena
global centena
global milhar

numero = int(input("insira o número"))

# servirá para verificar se a dezena esta entre 11 e 19

faixa_dezena = int(numero % 100)

unidade = int(numero % 10)
numero = (numero - unidade)/10
dezena = int(numero % 10)
numero = (numero - dezena)/10
centena = int(numero % 10)
numero = (numero - centena)/10
milhar = int(numero % 10)

# transforma em int para que consiga encontrar a posição no array

print("unidade :", unidade, "dezena:", dezena, "centena:", centena,
      "milhar:", milhar)


def verifica_milhar(milhar):
    if milhar != 0:
        mil = "mil"
        return mil


def verifica_centena(centena):
    centenas = ["cem", "duzentos", "trezentos", "quatrocentos", "quinhentos",
                "seissentos", "setessentos", "oitocentos", "novecentos", None]
    return centenas[centena]


def verifica_faixa_dezena(faixa_dezena, dezena):
    if (faixa_dezena > 10 and faixa_dezena < 20):
        posicao = int(faixa_dezena % 10)
        dezena_inicial = ["onze", "doze", "treze", "quatorze", "quinze",
                          "dezesseis", "desessete", "dezoito", "dezenove",
                          None]
        return dezena_inicial[posicao]
    else:
        dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
                   "sessenta", "setenta", "oitenta", "noventa", None]
        return dezenas[dezena]


def verifica_unidade(unidade):
    unidades = ["um", "dois", "três", "quatro", "cinco", "seis", "sete",
                "oito", "nove", None]
    return unidades[unidade]


print(verifica_milhar(milhar))
print(verifica_centena(centena))
print(verifica_faixa_dezena(faixa_dezena, dezena))
print(verifica_unidade(unidade))
