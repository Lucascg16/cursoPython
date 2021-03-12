termo = int(input('Digite o primeiro termo da P.A:'))
razao = int(input('Digite a razão da P.A:'))
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('FIM')
