lista = []
impares = []
pares = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Digite S ou N:')).strip().upper()[0]
    elif r in 'N':
        break
print(f'''A lista digitada foi {lista}. 
E tem o valores pares presentes: {pares}. 
E os valores imapares presentes: {impares}.''')