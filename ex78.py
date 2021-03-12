lista = []
mai = men = 0
for c in range(0, 5):
    lista.append(int(input('Digite um número:')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'O valor {mai} é o maior valor e aparece na posição ', end='')
for c, v in enumerate(lista):
    if v == mai:
        print(f'{c+1}...', end='')
print()
print(f'O valor {men} é o maior valor e aparece na posição ', end='')
for c, v in enumerate(lista):
    if v == men:
        print(f'{c+1}...',end='')
print()
