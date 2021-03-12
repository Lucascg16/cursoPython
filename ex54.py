from datetime import date
countmaior = 0; countmenor = 0
atual = date.today().year
for i in range(1, 8):
    id = int(input('Em que ano a {}ª pessoa nasceu:'.format(i)))
    if atual - id >= 18:
        countmaior = countmaior + 1
    else:
        countmenor = countmenor + 1
print('Temos {} pessoas maiores de idade.'.format(countmaior))
print('Temos {} pessoas menores de idade.'.format(countmenor))