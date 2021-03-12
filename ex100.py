from random import randint
from time import sleep
def sorteia(lista):
    for i in range(5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end='->')
        sleep(0.5)
    print('FIM')


def somapar(lista):
    soma = somatot = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
        somatot += valor
    print(f'Somando os valores pares o resultado é {soma}')
    print(f'A soma total dos valores da lista é {somatot}')

numeros = list()
sorteia(numeros)
somapar(numeros)