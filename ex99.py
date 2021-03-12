def maior(* num):
    mai = cont = 0
    for i in num:
        print(f'{i}', end='')
        if cont == 0:
            mai = i
        else:
            if i > mai:
                mai = i
        cont += 1
    print(f'{mai}...')


maior(2, 4, 1, 3, 1, 5, 7, 6)
