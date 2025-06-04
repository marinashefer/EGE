from ipaddress import *

ans = 0
for mask in range(10, 31):
    net1 = ip_network(f'95.24.2.9/{mask}', False)
    net2 = ip_network(f'95.24.3.10/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip_address('95.24.2.9') in net1.hosts() and ip_address('95.24.3.10') in net2.hosts():
            cnt1 = 0
            for i in net1.hosts():
                i = f'{int(i):032b}'
                if i[-1] == '0':
                    cnt1 += 1

            cnt2 = (net2.num_addresses - 2) // 2
            ans = max(ans, cnt1, cnt2)


print(ans)
