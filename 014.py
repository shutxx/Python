n = float(input('Qual valor do salario do funcionário? R$: '))
print('Com aumento de 15%, o funcionário que recebia R$:{:.2f}, vai receber R$:{:.2f}'.format(n, (n + (n * 15 / 100))))
