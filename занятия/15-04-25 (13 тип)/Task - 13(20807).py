from ipaddress import ip_network

net = ip_network(f'172.16.192.0/255.255.192.0')

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 5 != 0:
        cnt += 1

print(cnt)