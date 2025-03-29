from ipaddress import ip_address
from itertools import  groupby

with open ('26_3902.txt') as file:
    n = int(file.readline())
    ips = []
    for i in file:
        ip = f'{int(ip_address(('.'.join(i.split())))): 032b}'
        ips.append([ip[:19], ip[19:]])


ans_ip = ''
ans_cnt = 0
for ip in ans.items():
    if ans_cnt < len(i[1]):
        ans_cnt = len(i[1])
        ans_ip = i[0]

print(ans_ip, ans_cnt)