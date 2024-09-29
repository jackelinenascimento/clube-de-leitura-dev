class Stack:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("A pilha está vazia")

    def size(self):
        return len(self.itens)
    

stack = Stack()
stack.is_empty()