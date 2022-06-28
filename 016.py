d = int(input('Quantos dias o carro foi alugado: '))
k = float(input('Quantos quilômetros ele rodou?: '))
print('O total a pagar é de R$:{:.2f}'.format(d * 60.00 + k * 0.15))
