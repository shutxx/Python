n = float(input('Qual preço do produto? R$: '))
print('O produto que custava R$:{:.2f}, ma promoção vai custar R$:{:.2f}'.format(n, (n - (n * 5 / 100))))
