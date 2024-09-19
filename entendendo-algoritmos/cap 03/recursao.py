# Fatorial (Calculo de fatorial de um numero)
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)


# Fibonacci (Retorna o termo da sequencia de Fibonacci)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Soma de uma lista
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])


# Teste de Mesa
print(fatorial(1000))
print(fibonacci(7))
print(soma_lista([1, 2, 3, 4, 5]))
