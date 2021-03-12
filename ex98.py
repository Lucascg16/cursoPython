from time import sleep
def cont(inicio, fim, passo):
    print(f'Contando de {inicio} ate {fim} pulando de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f'{i}', end='->')
            sleep(0.5)
        print('Fim!')
    else:
        for i in range(inicio, fim - 1, passo * -1):
            print(f'{i}', end='->')
            sleep(0.5)
        print('Fim!')


cont(1, 10, 1)
cont(10, 1, 1)
ini = int(input('Valor de saida:'))
fim = int(input('Valor de chegada:'))
pas = int(input('Passo:'))
cont(ini, fim, pas)