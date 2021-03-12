soma = int(0)
cont = int(0)
for i in range(1, 501, 2):
    if i%3 == 0:
        soma = i + soma
        cont = cont + 1
print('A soma de {} valores impares divisivel por 3 ate 500 é {}'.format(cont, soma))