matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma = soma2 = mai = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    soma2 += matriz[l][2]
for c in range(3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares foi de {soma}')
print(f'A soma dos valores da terceira colula foi de {soma2}')
print(f'O maior valor da segunda coluna foi o {mai}')