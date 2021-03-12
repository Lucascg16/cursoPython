termo = int(input('Digite o primeiro termo da P.A:'))
razao = int(input('Digite a razão da P.A:'))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end ='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais:'))
print('fim, total de numeros printados na tela {}'.format(total))