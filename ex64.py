num = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]:'))
    if num != 999:
        soma = soma + num
print('A soma dos valores digitados {}'.format(soma))
