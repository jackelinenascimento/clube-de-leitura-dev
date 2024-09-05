## Exercícios

2.2 Suponha que você esteja criando um aplicativo para anotar os pedidos
dos clientes em um restaurante. Seu aplicativo precisa de uma lista de
pedidos. Os garçons adicionam os pedidos a essa lista e os chefes retiram
os pedidos da lista. Funciona como uma la. Os garçons colocam os
pedidos no nal da la e os chefes retiram os pedidos do começo dela
para cozinhá-los.
Você usaria um array ou uma lista encadeada para implementar essa lista?
(Dica: listas encadeadas são boas para inserções/eliminações e arrays são
bons para acesso aleatório. O que fazer neste caso?)

### R. Lista encadeada pois tem-se muitas inserções/eliminações e não tem acesso aleatório.

2.3 Vamos analisar um experimento. Imagine que o Facebook guarda uma
lista de usuários. Quando alguém tenta acessar o Facebook, uma busca é
feita pelo nome de usuário. Se o nome da pessoa está na lista, ela pode
continuar o acesso. As pessoas acessam o Facebook com muita
frequência, então existem muitas buscas nessa lista. Presuma que o
Facebook usa a pesquisa binária para procurar um nome na lista. A
pesquisa binária requer acesso aleatório – você precisa ser capaz de
acessar o meio da lista de nomes instantaneamente. Sabendo disso, você
implementaria essa lista como um array ou uma lista encadeada?

### R. Um array ordenado.

2.4 As pessoas se inscrevem no Facebook com muita frequência também.
Suponha que você decida usar um array para armazenar a lista de
usuários. Quais as desvantagens de um array em relação às inserções? Em
particular, imagine que você está usando a pesquisa binária para buscar
os logins. O que acontece quando você adiciona novos usuários em um
array?

### R. Nos arrays as inserções são lentas, e por conta da pesquisa binária, será necessário reordernar a lista sempre numa nova inserção.

2.5 Na verdade, o Facebook não usa nem arrays nem listas encadeadas para
armazenar informações. Vamos considerar uma estrutura de dados
híbrida: um array de listas encadeadas. Você tem um array com 26 slots.
Cada slot aponta para uma lista encadeada. Por exemplo, o primeiro slot
do array aponta para uma lista encadeada que contém os usuários que
começam com a letra A. O segundo slot aponta para a lista encadeada
que contém os usuários que começam com a letra B, e assim por diante.
Suponha que o Adit B se inscreva no Facebook e você queira adicioná-lo à
lista. Você vai ao slot 1 do array, a seguir para a lista encadeada do slot 1, e
adiciona Adit B no nal. Agora, suponha que você queira procurar o
Zakhir H. Você vai ao slot 26, que aponta para a lista encadeada de todos
os nomes começados em Z. Então, procura pela lista até encontrar o
Zakhir H. Compare esta estrutura híbrida com arrays e listas encadeadas. É mais lento
ou mais rápido fazer inserções e eliminações nesse caso? Você não precisa
responder dando o tempo de execução Big(O), apenas diga se a nova
estrutura de dados é mais rápida ou mais lenta do que os arrays e as listas
encadeadas.

R.

