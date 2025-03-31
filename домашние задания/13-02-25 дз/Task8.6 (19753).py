from itertools import product

cnt = 0
for val in product('0123456789', repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        if int(val) % 4 == 0:
                if val.count('0') <= 1 and val.count('1')<=1 and val.count('2') <= 1 and val.count('3')<=1 and val.count('4') <= 1 and val.count('5')<=1 and val.count('6') <= 1 and val.count('7')<=1 and val.count('8') <= 1 and val.count('9') <= 1:
                    val = val.replace('0', '*')
                    val = val.replace('2', '*')
                    val = val.replace('4', '*')
                    val = val.replace('6', '*')
                    val = val.replace('8', '*')
                    if '**' not in val:
                        cnt += 1

print(cnt)