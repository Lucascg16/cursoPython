from datetime import datetime
trab = dict()
trab['nome'] = str(input('Nome:'))
nascimento = int(input('Ano de nascimento:'))
trab['idade'] = datetime.now().year - nascimento
trab['carteira'] = int(input('Cartera de trabalho (0 caso não tenha!):'))
if trab['carteira'] != 0:
    trab['contratação'] = int(input('Ano de contratação:'))
    trab['salario'] = float(input('Salario: R$'))
    trab['aposentadoria'] = trab['idade'] + (trab['contratação'] + 40) - datetime.now().year
print('-=' * 30)
for i, v in trab.items():
    print(f'{i} = {v}')
