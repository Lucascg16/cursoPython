lista = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Digite S ou N:')).strip().upper()[0]
    elif r in 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} número.')
print(f'Essa é a lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado:')
else:
    print('Não foi encontrado o valor 5 na lista.')