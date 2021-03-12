num = (int(input('Digite um número:')), int(input('Digite um número:')), int(input('Digite um número:')),
       int(input('Digite um número:')))
print(f'Você Digitou os valores {num}')
print(f'O valor 9 aparece {num.count(9)} vezes na Tupla.')
if 3 in num:
    print(f'O valor 3 aparece na posição {num.index(3)+1}ª')
else:
    print('O valor 3 não aparece nos valores digitados')
print('Os valores pares digitados foram:', end= '')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')
