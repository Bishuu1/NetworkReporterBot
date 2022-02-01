from netmiko import ConnectHandler

huawei = {
    'device_type': 'huawei',
    'ip': 'AQUI_VA_LA_IP',
    'user': '',
    'pass': '',
    'port': 123,  # optional
    'secret:': 'secret'
}

net_connect = ConnectHandler(**huawei)

net_connect.enable()

list = ['display version', 'display mac-address', 'display arp', 'display ip routing-table',
        'display ip routing-table all-vpn-instance', 'display interface brief', 'display ip interface brief',
        'display ospf peer brief', 'display ospf interface']

for command in list:
    output = net_connect.send_command(command)
    f = open(command+".txt", "w+")
    f.write(output)
    f.close()
