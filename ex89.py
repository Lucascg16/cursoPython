notas = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota2:'))
    media = (nota1 + nota2) / 2
    notas.append([nome, [nota1, nota2], media])

    r = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Digite S ou N:')).strip().upper()[0]
    elif r in 'N':
        break
for i, l in enumerate(notas):
    print(f'Aluno {i:<4} Nome:{l[0]:<10} media:{l[2]:<8.1f}')
mais = 0
while mais != 999:
    mais = int(input('Mostrar as notas de qual aluno? [999 para]:'))
    if mais <= len(notas) -1:
        print(f'As notas do aluno {notas[mais][0].upper()} são {notas[mais][1]}')
