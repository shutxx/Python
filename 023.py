# import random
from random import shuffle
a1 = str(input('Digite nome do primeiro aluno: '))
a2 = str(input('Digite nome do segundo aluno: '))
a3 = str(input('Digite nome do terceiro aluno: '))
a4 = str(input('Digite nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
# random.shuffle(lista)
shuffle(lista)
print('Ordem de apresentação')
print(lista)
