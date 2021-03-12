from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for i in n:
    print(f' {i}', end= '')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
print(f'Os números sorteados em ordem crescente :{sorted(n)}')