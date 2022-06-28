# import math
from math import floor, ceil, sqrt

n = int(input('Digite um numero: '))
# raiz = math.sqrt(n)
raiz = sqrt(n)
# print('A raiz de {}, aredondada pra baixo é igual a {}'.format(n, math.floor(raiz)))
print('A raiz de {}, aredondada pra baixo é igual a {}'.format(n, floor(raiz)))

# print('A raiz de {}, aredondada pra cima é igual a {}'.format(n, math.ceil(raiz)))
print('A raiz de {}, aredondada pra cima é igual a {}'.format(n, ceil(raiz)))

print('A raiz total de {} é igual a {:.2f}'.format(n, raiz))
# linhas comentadas usam a biblioteca toda
