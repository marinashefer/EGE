from ipaddress import *

for mask in range(10, 31)[::-1]:
    net1 = ip_network(f'200.154.190.12/{mask}', False)
    net2 = ip_network(f'200.154.184.0/{mask}', False)
    if net1.network_address == net2.network_address:
        if ip_address('200.154.190.12') in net1.hosts() and ip_address('200.154.184.0') in net2.hosts():
            print(mask)
            break