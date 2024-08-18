import math

# Suponha que você tenha uma lista com 128 nomes e esteja fazendo
# uma pesquisa binária. Qual seria o número máximo de etapas que você
# levaria para encontrar o nome desejado?

NOMES = 128
ETAPAS = math.log2(NOMES)
print(ETAPAS)


# Suponha que você duplique o tamanho da lista. Qual seria o número
# máximo de etapas agora?

NOMES = 256
max_steps = math.log2(NOMES)
print(ETAPAS)