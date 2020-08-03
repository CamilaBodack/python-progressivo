
'''
Conversão de números para palavras Desafio

Na linguagem de sua preferência, crie um servidor HTTP que, para cada
requisiçãoGET, retorne um JSON cuja chave extenso seja a versão por extenso
do númerointeiro enviado no path. Os números podem estar no intervalo
[-99999, 99999].
Exemplos: λ curl http://localhost:3000/1 { "extenso": "um" }
λ curl http://localhost:3000/-1042 { "extenso": "menos mil e quarenta e dois" }
λ curl http://localhost:3000/94587 { "extenso": "noventa e quatro mil e
quinhentos e oitenta e sete" } Nos mande o link do repositório no GitHub com o
código em até sete dias. Se você abrir um Pull Request (p.ex. do seu branch de
desenvolvimento para o master) nós faremos o review e você terá a chance de
corrigir os erros para uma segunda avaliação. Não esqueça do README.md com
as instruções para rodar o servidor! Não esqueça dos "e"s separando milhares,
centenas e dezenas (vide exemplo): "noventa e quatro mil e quinhentos e oitenta
e sete". Esse não é o padrão da norma culta da língua portuguesa,
e isso é intencional. É esperado que você implemente o algoritmo de tradução.
Mesmo que não esteja com a lógica completa, nos envie o que conseguiu fazer até
o momento.
'''


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

verifica_dezena = int(numero % 100)

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


def verifica_faixa_dezena(verifica_dezena):
    # verificar posicao entre 11 e 19
    if (verifica_dezena > 10 and verifica_dezena < 20):
        dezena_inicial = ["onze", "doze", "treze", "quatorze", "quinze",
                          "dezesseis", "desessete", "dezoito", "dezenove",
                          None]
        return dezena_inicial[verifica_dezena]
    else:
        dezena = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
                  "sessenta", "setenta", "oitenta", "noventa", None]
        return dezena[verifica_dezena]


def verifica_unidade(unidade):
    unidades = ["um", "dois", "três", "quatro", "cinco", "seis", "sete",
                "oito", "nove", None]
    return unidades[unidade]


verifica_milhar(milhar), verifica_centena(centena), verifica_dezena(dezena),
verifica_unidade(unidade), verifica_faixa_dezena(verifica_dezena)
