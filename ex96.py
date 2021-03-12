def area(larg,comp ):
    area  = larg * comp
    print(f'A área do terreno {larg}x{comp} é {area}')



#programa principal
l = float(input('Digite a largura do terreno(m):'))
c = float(input('Digite o comprimento do terreno(m):'))
area(l, c)
