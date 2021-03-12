num = (int(input('Digite um numero para ver a tabuada dele:')))
for i in range(1, 11):
    print('{} X {:2} = {}'.format(num, i, num*i))