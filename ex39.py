from datetime import date
atual = date.today().year
ano = int(input('Digite o ano que voçê nasceu:'))
idade = atual -  ano
#print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Voçê tem que se alistar neste ano')
elif idade < 0:
    print('Posso prever o futuro, mas isso vai demorar um pouco mais do que deveria.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voçê deveria se alistado a {} anos '.format(saldo))
