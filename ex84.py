temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(int(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Digite S ou N:')).strip().upper()[0]
    elif r in 'N':
        break
print(f'Total de pessoas cadastradas: {len(princ)}')
print(f'O maior peso foi de {mai}, nome:', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}, nome:',end=' ')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()
