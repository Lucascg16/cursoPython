def lin(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva = str(input('Digite uma mensagem:'))
lin(escreva)