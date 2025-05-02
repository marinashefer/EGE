from itertools import product

cnt = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[-1] not in '347':
        if '000' not in val and '111' not in val and '222' not in val and '333' not in val and '444' not in val and '555' not in val and '666' not in val and '777' not in val and '888' not in val:
            if val[0] != '0':
                cnt += 1

print(cnt)