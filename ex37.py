num = int(input('Digite um número inteiro:'))
print('''Escolha uma base para converter
1 para octal
2 para hexadecimal
3 para binario''')
op = int(input('Sua opção:'))
if op == 1:
    print('O número {} é {} em octal'.format(num, oct(num)[2:]))
elif op == 2:
    print('O número {} é {} em hexadecimal'.format(num, hex(num)[2:]))
else:
    print('O número {} é {} em binario'.format(num, bin(num)[2:]))