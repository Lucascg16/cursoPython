from random import randint
v = 0
print('Par ou Impar')
while True:
    pe = int(input('Digite um numero:'))#pe = pessoa
    pc = randint(1, 10)
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar [P/I]:')).strip().upper()[0]#pi = par ou impar
    soma = pc + pe
    print(soma)
    if pi == 'P':
        if soma % 2 == 0:
            print('Jogador ganha.')
            v += 1
        else:
            print('Jogador perde.')
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print('Jogador ganha.')
            v += 1
        else:
            print('Jogador perde.')
            break
    print('Vamos jogar novamente:')
print(f'Game Over, Você venceu {v} vezes.')
