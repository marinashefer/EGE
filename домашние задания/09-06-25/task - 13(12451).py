from ipaddress import *

cnt = 0
for a in range(0, 256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', False)
    for i in net:
        i = f'{int(i):032b}'
        if not (i[16:24].count('0') > i[24:].count('0')):
            break
    else:
        cnt += 1

print(cnt)