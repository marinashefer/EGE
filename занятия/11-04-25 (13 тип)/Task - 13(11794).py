from ipaddress import ip_network

for a in range(256)[::-1]:
    net = ip_network(f'223.167.{a}.167/26', False)
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') > i[16:].count('0'):
            break
    else:
        print(a)
        break