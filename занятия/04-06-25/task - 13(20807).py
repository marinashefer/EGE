from ipaddress import *

cnt = 0
net = ip_network('172.16.192.0/255.255.192.0', False)
for ip in net:
    i = f'{int(ip):032b}'
    if i.count('1') % 5 != 0:
        cnt += 1

print(cnt)
