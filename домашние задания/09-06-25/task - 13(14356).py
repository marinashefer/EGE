from ipaddress import *

ans = []
for a in range(0, 256)[::-1]:
    net = ip_network(f'217.109.{a}.94/255.255.254.0', False)
    for i in net:
        i = f'{int(i):032b}'
        if not (i[:16].count('0') <= i[16:].count('0')):
            break
    else:
        print(a)
        break

