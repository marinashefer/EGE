from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0', False)
cnt = 0
for ip in net:
    i = f'{int(ip):032b}'
    if i.count('1') % 2 != 0:
        cnt += 1

print(cnt)