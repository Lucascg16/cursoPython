a = str('*')
con = 0
while (con < 5):
    for cont in range(1, 10):
        print(a*cont)
    for i in range(10, 0, -1):
        print(a*i)
    con += 1
