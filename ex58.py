from random import randint
count = 0
num = randint(0, 10)
uso = int(input('Digite um numero entre 0 e 10:'))
while uso != num:
    if num > uso:
        uso = int(input('Maior, digite outro número:'))
    else:
        uso = int(input('Menor, digite outro número:'))
    count = count + 1
print('Acertou com {} tentativas. parabens.'.format(count))
