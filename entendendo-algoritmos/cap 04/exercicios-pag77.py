#4.1 Escreva o código para a função soma, vista anteriormente.

def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma([1, 2, 3, 4, 5]))


#4.2 Escreva uma função recursiva que conte o número de itens em uma lista.

def contar(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + contar(lista[1:])

print(contar([1, 2, 3, 4, 5]))

#4.3 Encontre o valor mais alto em uma lista.

def maior(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        maior_numero = maior(lista[1:])
        if lista[0] > maior_numero:
            return lista[0]
        else:
            return maior_numero

print(maior([1, 2, 7, 4, 5]))

#4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um
#algoritmo do tipo dividir para conquistar. Você consegue determinar o
#caso-base e o caso recursivo para a pesquisa binária?

# Caso base: Se a lista estiver vazia, retorne False
# Caso recursivo: Se o item do meio da lista for igual ao item que estamos
# procurando, retorne True. Se o item do meio for maior que o item que estamos
# procurando, chame a função novamente com a primeira metade da lista. Se o
# item do meio for menor que o item que estamos procurando, chame a função
# novamente com a segunda metade da lista.

#4.5 Implemente a pesquisa binária em Python.

def pesquisa_binaria(lista, item):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista) // 2
        if lista[meio] == item:
            return True
        else:
            if lista[meio] > item:
                return pesquisa_binaria(lista[:meio], item)
            else:
                return pesquisa_binaria(lista[meio+1:], item)

print(pesquisa_binaria([1, 2, 3, 4, 5], 3))