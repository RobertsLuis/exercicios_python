"""
Questão **Inspiração:
Linked Lists - Length & Count
Implement Length() to count the number of nodes in a linked list.

Como resolução, criei uma lista duplamente encadeada, com outros métodos essenciais, incluindo o solicitado pela questão
"""


from ListaDuplamenteEncd import ListaDupla, Aluno

lista = ListaDupla()
lista.add_begin(Aluno("João"))
lista.add_end(Aluno("Maria"))
lista.add_in_pos(Aluno("Pedro"), 1)
lista.remove_begin()
lista.remove_end()