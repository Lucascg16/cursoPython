listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Tranferdor', 4.50,
            'Compasso', 9.99,
            'Mochila', 111.99,
            'Caneta', 2.99,
            'Livro', 23.99)
print('-'*40)
print(f'{"Lista de Preços":^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end= '')
    else:
        print(f'R${listagem[item]:>6.2f}')
print('-'*40)
