for n in range(1, 10000):
    r = bin(n)[2:]
    r = r.replace('1', '0').replace('0', '1')
    r = '1' + r
    if r.count('1') % 2 == 0:
        r = r + '0'
    else:
        r = r + '1'

    if int(r, 2) > 180:
        print(n)
        break