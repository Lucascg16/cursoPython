n = ('Zero', 'Um' ,'Dois', 'Três', 'Quatro',
     'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
     'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
     'Quize', 'Dezesseis', 'Dezessete', 'Dezoito',
     'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um Número entre 0 e 20:'))
    if 0 <= num <= 20:
        print(f'Você digitou o número {n[num]}')
    else:
        print('Tente Novamente.', end=' ')
    cont1nue = ' '
    while cont1nue not in 'SN':
        cont1nue = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont1nue == 'N':
        break