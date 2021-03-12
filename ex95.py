time = list()
jog = dict()
partidas = list()

while True:
    jog.clear()
    jog['jogador'] = str(input('Nome do jogador:'))
    tot = int(input('Numero de jogos:'))
    partidas.clear()
    for i in range(tot):
        partidas.append(int(input(f'O numero de gols feitos na {i+1}ª partida:')))
    jog['gols'] = partidas[:]
    jog['total'] = sum(partidas)
    time.append(jog.copy())
    while True:
        r = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar os dados de qual jogados? (999 desliga):'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Jogador não encontrado...')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i} fez {g} gols')
print('-'*40)
