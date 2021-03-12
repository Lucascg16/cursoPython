sexo = str(input('Digite o seu sexo [M/F}:')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
#while sexo not in 'MF':
    sexo = str(input('Valor invalido, por favor digite o seu sexo[M/F]:')).strip().upper()[0]
print('Sexo {} foi registrado com sucesso.'.format(sexo))