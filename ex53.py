frase = str(input('Digite uma frase:')).upper().strip()
palavras =frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
    if inverso == junto:
        print('Temos um palindromo.')
        print(junto, inverso)
    else:
        print('A frase Digitada não é um palindromo;')

