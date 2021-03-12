from random import randint
print('Pedra, papel, tesoura!!!')
itens = ('Pedra', 'Papel', 'Tesoura')
jog = int(0)
countmac = int(0)
countjog = int(0)
for i in range(0, 6):
    mac = randint(0, 2)
    jog = int(input('''
    0 = Pedra;
    1 = Papel;
    2 = Tesoura;
    Sua opção:'''))
    print('O computador escolheu {}'.format(itens[mac]))
    print('O jogador jogou {}'.format(itens[jog]))
    if mac == 0:
        if jog == 0:
            print('Empate.')
        elif jog == 1:
            print('Jogador ganhou.')
            countjog += 1
        elif jog == 2:
            print('jogador perde.')
            countmac += 1
        else:
            print('Jogada invalida.')
    elif mac == 1:
        if jog == 0:
            print('Jogador perde.')
            countmac += 1
        elif jog == 1:
            print('Empate.')
        elif jog == 2:
            print('jogador ganha.')
            countjog += 1
        else:
            print('Jogada invalida.')
    elif mac == 2:
        if jog == 0:
            print('Jogador ganha.')
            countjog += 1
        elif jog == 1:
            print('Jogador Perde.')
            countmac += 1
        elif jog == 2:
            print('Empate.')
        else:
            print('Jogada invalida.')
    print ('Placar = jogador {} x maquina {}'.format(countjog, countmac))