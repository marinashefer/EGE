from ipaddress import ip_address, ip_network

net = ip_network('192.168.31.80/255.255.255.240')
ans = []
for i in net:
    i = f'{int(i):032b}'
    ans.append(i.count('1'))

print(max(ans))