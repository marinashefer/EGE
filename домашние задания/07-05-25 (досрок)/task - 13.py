from ipaddress import ip_network, ip_address

net = ip_network('143.168.72.213/255.255.255.240', False)

ans = []
for i in net:
    if i != net.broadcast_address and i != net.network_address:
        ans.append(i)

print(max(ans))