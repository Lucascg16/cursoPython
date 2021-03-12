jog = dict()
partidas = list()
jog['jogador'] = str(input('Nome do jogador:'))
tot = int(input('Numero de jogos:'))
for i in range(tot):
    partidas.append(int(input(f'O numero de gols feitos na {i+1}ª partida:')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)
print('-=' * 30)
print(jog)
print('-=' * 30)
for k, v in jog.items():
    print(f'{k} é {v}')
print('-=' * 30)