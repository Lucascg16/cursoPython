from time import sleep
brasileirao=('Flamengo', 'Santos', 'Palmeiras', 'Gremio','AthleticoParanaense', 'SãoPaulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'VascodaGama', 'AtléticoMG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('=' * 25)
print('Programa do Brasileirao!!')
print('=' * 25)

while True:
    opcao = (input('Escolha uma das seguintes opcoes: \n'
                      '[1] - Mostrar a classificacao\n'
                      '[2] - Mostrar os 5 primeiros\n'
                      '[3] - Mostrar os rebaixados\n'
                      '[4] - Times em ordem alfabetica\n'
                      '[5] - Chapecoense \n'
                      '[6] - Sair \n'
                      'Digite o numero da opcao: '))
    while opcao not in '123456':
        print('Opcao invalida.')
        opcao = int(input('Escolha uma das seguintes opcoes: \n'
                          '[1] - Mostrar a classificacao\n'
                          '[2] - Mostrar os 5 primeiros\n'
                          '[3] - Mostrar os rebaixados\n'
                          '[4] - Times em ordem alfabetica\n'
                          '[5] - Posicao da Chapecoense \n'
                          '[6] - Sair \n'
                          'Digite o numero da opcao: '))
    if opcao == '1':
        print('Esta foi a classificacao do Brasileirao 2019')
        for pos, c in enumerate (brasileirao):
            print(f' {pos+1} {c}')
    if opcao == '2':
        print('Estes sao os 5 primeiros colocados:')
        for pos, cont in enumerate (brasileirao[0:5]):
            print(f'{pos+1} {cont}')
    if opcao == '3':
        print('Estes foram os rebaixados:')
        for z4 in (brasileirao[-4:]):
            print(f'{z4}')
    if opcao == '4':
        print("Estes sao os times que participaram em ordem alfabetica:")
        print(sorted(brasileirao))
    if opcao == '5':
        print('Esta foi a posicao do time da Champecoense este ano:')
        for pos, c in enumerate (brasileirao):
            if c == 'Chapecoense':
                print(f' {pos+1} {c}')
    if opcao == '6':
        print('Voce escolheu sair do programa.')
        break
    continuar=str(input('Quer Continuar? [SN]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Opcao invalida')
        continuar = str(input('Quer Continuar? [SN]')).upper().strip()[0]
    if continuar == 'N':
        break
    sleep(1)
    print('=' * 25)
print('Fim do programa, obrigado.')