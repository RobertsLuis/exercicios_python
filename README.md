# exercicios_python
Conjunto de exercício retirado do CodeWars ou Hackerrank, para exercitar conceitos básicos da linguagem e versionamento de códigos.

Questão 1 (Strings - regex, list comprehension, testes unitários):
  https://www.codewars.com/kata/6512b3775bf8500baea77663
  
    Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
    Note that if the range is given in capital letters, return the string in capitals also!
      Entry: 
      A-A
      
      Output:
      ABCDEFGHIJKLMNOPQRSTUVWXYZa
      

Questão 2 (Strings - list comprehension, testes unitários):
  https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
  
    You are given a string, line width and paragraph height.
    Your task is to wrap the string into paragraph(s).
    **You can't return a half word
    
      Entry: 
      Cinco Cinco Cinco Cinco cinco, 12, 2
      
      Output: 
      Cinco Cinco
      Cinco Cinco

      Cinco
      
Questão 3 (Estrutura de dados - POO):
  Crie uma lista duplamente encadeada para armazenar alunos
  
      **Inspiração
      https://www.codewars.com/kata/linked-lists-length-and-count
      Linked Lists - Length & Count
      Implement Length() to count the number of nodes in a linked list.

Questão 4 (Listas, tuplas, dicionario):

    We need a function that receives an array or list of integers (positive and negative) and may give us the following information in the order and structure presented below:
    [(1), (2), (3), [[(4)], 5]]
      (1) - Total amount of received integers.
      (2) - Total amount of different values the array has.
      (3) - Total amount of values that occur only once.
      (4) and (5) both in a list
        (4) - It is (or they are) the element(s) that has (or have) the maximum occurrence. If there are more than one, the elements should be sorted (by their value obviously)
        (5) - Maximum occurrence of the integer(s)

    Entry:
    [0,0,0,1,2,3,4]
    Output:
    [[7, 5, 4, [[0], 3]]]
