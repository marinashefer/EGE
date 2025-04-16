from ipaddress import ip_network, ip_address

cnt = 0
ip = ip_address('218.48.192.0')
for mask in range(33):
    net = ip_network(f'218.48.192.56/{mask}', False)
    if net.num_addresses >= 502 and ip == net.network_address:
        cnt += 1

print(cnt)
# net.broadcast_addressне не является широковщ.
# ip != net.network_address не является адресом сети