def leiaInt(msg):
    while True:
        try:
            ni = int(input(msg))
        except(ValueError, TypeError):
            print('Erro. Digite um número valido.')
            continue
        except(KeyboardInterrupt):
            print('Valor não informado.')
            return 0
        else:
            return ni


def leiaFloat(msg):
    while True:
        try:
            nf = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO. Digite um valor valido.')
        except(KeyboardInterrupt):
            print('Valor não informado.')
            return 0
        else:
            return nf


n = leiaInt('Digite um numero:')
n2 = leiaFloat('Digite outro número')
print(f'O número digitado foi {n} e {n2}')
