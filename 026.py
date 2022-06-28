frase = str(input('Digite seu nome completo: ')).strip()
print('Seu nome maiúsculas é: {}'.format(frase.upper()))
print('Seu nome em minúsculas é: {}'.format(frase.lower()))
print('Seu nome ao todo tem: {} letras'.format(len(frase)-frase.count(' ')))
print('Seu primeiro nome tem tantas letras: {}'.format(frase.find(' ')))
print(frase.replace(" ", ""))
separa = frase.split()
print('Seu primeiro nome é : {} e ele tem tem {} letras'.format(separa[0], len(separa[0])))

