soma = 0
for i in range(1, 7):
    num = int(input('Digite um {}° valor:'.format(i)))
    if num % 2 == 0:
        soma = soma + num
    print(soma)