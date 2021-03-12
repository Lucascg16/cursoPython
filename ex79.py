lista = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Armazenado com sucesso...')
    else:
        print('O número digitado ja existe e não será armazenado!')
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r in 'SN':
        if r == 'N':
            break
    else:
        print('Digite S ou N por favor!')

lista.sort()
print(f'Voçê digitou os valores {lista}')