# Arrays em Python

Em Python, um array é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo. Os arrays em Python são implementados pela classe `array` do módulo `array`.

## Criando um array

Para criar um array em Python, você precisa importar o módulo `array` e usar a função `array()` passando o tipo de dado dos elementos e os valores do array.

Exemplo:

```python
from array import array

# Criando um array de inteiros
meu_array = array('i', [1, 2, 3, 4, 5])

# Criando um array de floats
outro_array = array('f', [1.5, 2.7, 3.9])
```

## Acessando elementos do array

Os elementos de um array em Python podem ser acessados usando índices. O primeiro elemento tem índice 0, o segundo tem índice 1 e assim por diante.

Exemplo:

```python
from array import array

meu_array = array('i', [1, 2, 3, 4, 5])

# Acessando o primeiro elemento
primeiro_elemento = meu_array[0]

# Acessando o terceiro elemento
terceiro_elemento = meu_array[2]
```

## Modificando elementos do array

Os elementos de um array em Python podem ser modificados atribuindo um novo valor a um índice específico.

Exemplo:

```python
from array import array

meu_array = array('i', [1, 2, 3, 4, 5])

# Modificando o segundo elemento
meu_array[1] = 10

# Modificando o quarto elemento
meu_array[3] = 20
```

## Tamanho do array

Você pode obter o tamanho de um array em Python usando a função `len()`.

Exemplo:

```python
from array import array

meu_array = array('i', [1, 2, 3, 4, 5])

# Obtendo o tamanho do array
tamanho = len(meu_array)
```