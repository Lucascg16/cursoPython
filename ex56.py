countiade = 0
media = 0
maidade = 0
nomevelho = ''
countmu = 0
for i in range(1, 5):
    print('------ {}ª Pessoa ------'.format(i))
    nome = str(input('Digite o seu nome:')).strip()
    idade = int(input('Digite a sua idade:'))
    sexo = str(input('sexo[M/F]:')).strip()
    countiade = countiade + idade
    if i == 1 and sexo in 'Mm':
        maidade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maidade:
        maidade = idade
        nomevelho = nome
    if sexo in 'Ff':
        if idade < 20:
            countmu = countmu +1
media = countiade / 4
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho é o {} e tem {} anos.'.format(nomevelho, maidade))
print('Numero de mulheres menores de 20 é {}'.format(countmu))