n = cont = 0
while True:
    n = int(input('Digite um numero para ver a tabuada dele:'))
    if n < 0:
        break
    while cont < 11:
        mult = n * cont
        print(f'{n} X {cont} = {mult}')
        cont += 1
