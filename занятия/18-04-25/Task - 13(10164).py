from ipaddress import ip_address, ip_network

ip = ip_address('156.132.15.138')
net = ip_network('156.132.15.138/255.255.252.0', False)

for pos, val in enumerate(net):
    if val == ip:
        print(pos)


