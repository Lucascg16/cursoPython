idade = maidade = qtdhomem = menidade = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade > 18:
        maidade += 1
    if sexo == 'M':
        qtdhomem += 1
    if sexo == 'F' and idade > 20:
        menidade += 1
    cont1nue = ' '
    while cont1nue not in 'NS':
        cont1nue = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if cont1nue == 'N':
        break
print(f'O número de pessoas cadastradas acima de 18 anos foi de {maidade}')
print(f'O número de homens cadastrados foi de {qtdhomem}')
print(f'O número de mulheres abaixo de 20 anos foi de {menidade}')