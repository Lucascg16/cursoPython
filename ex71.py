from time import sleep
valor = int(input('Digite o valor a ser sacado:'))
cont50 = cont10 = cont5 = cont1 = 0
while valor > 0:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    else:
        if valor >= 10:
            valor -= 10
            cont10 += 1
        else:
            if valor >= 5:
                valor -= 5
                cont5 += 1
            else:
                if valor >= 0:
                    valor -= 1
                cont1 += 1
print(f'O valores sacados foram {cont50} notas de 50\n'
      f'{cont10} notas de 10\n{cont5} notas de 5\n{cont1} notas de 1.')
print('Fechando o aplicativo...')
sleep(2)