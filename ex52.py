num = int(input('Digite um número:'))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(i), end=' ')
if tot == 2:
    print('\nO numero {} é primo.'.format(num))
else:
    print('\nO numero {} não é primo.'.format(num))
