from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', False)

cnt = 0
for ip in net:
    i = f'{int(ip):032b}'
    if i.count('1') % 3 != 0:
        cnt += 1

print(cnt)