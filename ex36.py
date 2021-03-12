nome = str(input('Digite o seu nome:'))
print('Bom dia {}'.format(nome))
print('Primeiramente preciso que digite algumas informaçõe.')
valor = int(input('Digite o valor da casa a ser comprada:'))
sal = int(input('Digite o seu salario:'))
ano = int(input('Por quantos anos deseja estar apagando:'))
valmes = valor / (ano * 12)
persal = sal * 0.30
if valmes > persal:
    print('Infelizmente não podemos fechar negocio.')
else:
    print('Parabens {}, o valor a ser pago por mes é de {}, nos próximos {} anos'.format(nome, valmes, ano))