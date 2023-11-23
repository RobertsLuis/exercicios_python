class Nodo:
    def __init__(self, aluno):
        self.aluno = aluno
        self.proximo = None
        self.anterior = None


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.ID = None
    def __str__(self):
        return f"ID: {self.ID}, Nome: {self.nome}"


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def add_begin(self, aluno):
        novo_no = Nodo(aluno)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

        self.tamanho += 1
        self.exibir()

    def add_end(self, aluno):
        novo_no = Nodo(aluno)
        if self.inicio is None:
            self.add_begin(aluno)
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
            self.tamanho += 1

        self.exibir()

    def add_in_pos(self, aluno, pos):
        if pos < 0 or pos > self.tamanho:
            print("Adição não efetuada, posição inválida")
            return

        novo_no = Nodo(aluno)
        if pos == 0:
            self.add_begin(aluno)
            return
        elif pos == self.tamanho:
            self.add_end(aluno)
            return
        else:
            i = 0
            atual = self.inicio
            while i != pos:
                atual = atual.proximo
                i += 1
            atual.anterior.proximo = novo_no
            atual.anterior = novo_no
            novo_no.proximo = atual

        self.tamanho += 1
        self.exibir()

    def remove_begin(self):
        self.inicio.proximo.anterior = None
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        self.exibir()

    def remove_end(self):
        self.fim.anterior.proximo = None
        self.fim = self.fim.anterior
        self.tamanho -= 1
        self.exibir()

    def remove_by_pos(self, pos):
        if pos < 0 or pos > self.tamanho - 1:
            print("Remoção não efetuada, posição inválida")
            return

        if pos == 0:
            self.remove_begin()
            return
        elif pos == self.tamanho - 1:
            self.remove_end()
            return
        else:
            i = 0
            atual = self.inicio
            while i != pos:
                atual = atual.proximo
                i += 1
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior

        self.tamanho -= 1
        self.exibir()

    def remove_by_element(self, aluno):
        atual = self.inicio
        while atual.aluno.ID != aluno.ID and atual.proximo is not None:
            atual = atual.proximo
        if atual.aluno.ID != aluno.ID:
            print("Aluno não está na lista")
            return
        elif aluno.ID == 0:
            self.remove_begin()
            return
        elif aluno.ID == self.tamanho - 1:
            self.remove_end()
            return
        else:
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior

        self.tamanho -= 1
        self.exibir()

    def exibir(self):
        self.__rearangeIds()
        atual = self.inicio
        print("\nLista de alunos:")
        while atual is not None:
            print(atual.aluno)
            atual = atual.proximo
        print("Tamanho total:", self.tamanho)
        print("Inicio:", self.inicio.aluno.nome, "\nFim:", self.fim.aluno.nome, "\n")

    def __rearangeIds(self):
        i = 0
        atual = self.inicio
        while atual is not None:
            atual.aluno.ID = i
            atual = atual.proximo
            i += 1