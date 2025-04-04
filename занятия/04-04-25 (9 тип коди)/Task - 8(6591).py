from itertools import *

cnt = 0
for val in product('0123456', repeat = 5):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('6') == 1:
            cnet = 0
            nechet = 0
            for i in val:
                if int(i) % 2 == 0:
                    cnet += int(i)
                else:
                    nechet += int(i)
            if cnet < nechet:
                cnt += 1

print(cnt)
