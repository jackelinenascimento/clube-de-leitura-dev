class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.itens)
    
pilha = Pilha()
pilha.append(1)
