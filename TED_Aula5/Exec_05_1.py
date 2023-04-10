numero = int(input('Digite um numero entre 1000 e 2000: '))
if numero in range(1000, 2000+1):
    print('{} está no intervalo'.format(numero))
else:
    print('{} está fora do intervalo'.format(numero))