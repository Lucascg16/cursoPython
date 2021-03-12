galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, Digite M ou F')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
        if r in 'SN':
            break
        print('S ou N por favor.')
    if r in 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A media de idade do grupo é de {media:5.2f} anos')
print('As mulheres cadastradas foram:', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('Pessoas com a idade acima da media:',end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end='')
print()
