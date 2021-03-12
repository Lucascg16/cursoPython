pa = (str(input('Digite uma palavra para saber as suas vogais:')),
      str(input('Digite uma palavra para saber as suas vogais:')))
for i in pa:
    print(f'\nNa paravra {i.upper()} temos as vogais',end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')
