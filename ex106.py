from time import sleep


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    titulo('Sistma de ajuda pyhelp')
    sleep(0.5)
    comando = str(input('Função ou biblioteca [exit para parar o programa]> '))
    if comando.upper() == 'EXIT':
        break
    else:
        ajuda(comando)
titulo('Fim do programa')
sleep(0.5)