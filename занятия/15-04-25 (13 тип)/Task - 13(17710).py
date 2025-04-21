from ipaddress import ip_network

net = ip_network('214.187.224.0/255.255.224.0')

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if int(i.count('1')) % 6 != 0 and i[-4:] == '1000':
        cnt += 1

print(cnt)