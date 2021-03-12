#outra de flag, so que com break...
n = cont = soma = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'O total de numero digitados foi {cont} e o a soma deles foi {soma}')