totva = menva = cont = contmi = 0
nome = menornome = ' '
while True:
    nome = str(input('O que você comprou:'))
    valor = int(input('Digite o valor do produto comprado:'))
    cont += 1
    if cont == 1:
        menva = valor
        menornome = nome
    if valor < menva:
        valor = menva
        menornome = nome
    if valor > 1000:
        contmi += 1
    totva += valor
    cont1nue = ' '
    while cont1nue not in 'SN':
        cont1nue = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if cont1nue == 'N':
        break
print(f'O valor total da compra foi de {totva}')
print(f'O numero de produtos com o valor maior de 1000R$:{contmi}')
print(f'O produto mais barato foi o {menornome}')
