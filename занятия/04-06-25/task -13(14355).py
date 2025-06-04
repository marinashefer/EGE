from ipaddress import *

for mask in range(16, 25):
    net =ip_network(f'127.63.67.1/{mask}', False)
    for ip in net:
        i = f'{int(ip):032b}'
        if not (i[:16].count('1') >= i[16:].count('1')):
            break
    else:
        print(net.netmask)
        break
