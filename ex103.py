def camp(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome}, fez {gols} gols no campionato')


n = str(input('Nome do jogador:'))
g = str(input('Numero de gols na temporada:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    camp(gols=g)
else:
    camp(n, g)