from ipaddress import ip_address, ip_network

ip = ip_address('143.131.211.37')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', False)
    cnt = 0
    for i in net:
        i = f'{int(i):032b}'
        if i.count('1') == 10:
            cnt += 1
        if cnt > 15:
            break
    if cnt == 15:
        print(mask)

