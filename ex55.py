maipeso = 0
menpeso = 0
for i in range(1, 6):
    peso = int(input('Digite o valor da {}ª pessoa:'.format(i)))
    if i == 1:
        menpeso = peso
    else:
        if peso > maipeso:
            maipeso = peso
        elif peso < menpeso:
            menpeso = peso
print('O maior peso lido foi de {}KG'.format(maipeso))
print('O menor peso lido foi de {}KG'.format(menpeso))