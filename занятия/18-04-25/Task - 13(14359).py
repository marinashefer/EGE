from ipaddress import ip_network, ip_address

ip1 = ip_address('157.127.172.56')
ip2 = ip_address('157.127.191.78')

for mask in range(33):
    net1 = ip_network(f'157.127.172.56/{mask}', False)
    net2 = ip_network(f'157.127.191.78/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip1 != net1.network_address and ip1 != net1.broadcast_address:
            if ip2 != net2.network_address and ip2 != net2.broadcast_address:
                print(mask)
                break



