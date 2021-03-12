num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
escolha = 0
while escolha != 5:
    escolha = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] maior número
    [4] Novos números
    Sua escolha:'''))
    if escolha == 1:
        soma = num1 + num2
        print('A soma entre {} e {} = {}'.format(num1, num2, soma))
    elif escolha == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} = {}'.format(num1, num2, mult))
    elif escolha == 3:
        if num1 > num2:
            print('O numero {} é maior'.format(num1))
        else:
            print('O numero {} é maior'.format(num2))
    elif escolha == 4:
        num1 = int(input('Digite um numero:'))
        num2 = int(input('Digite outro numero:'))
    else:
        print('Opção invalida.')