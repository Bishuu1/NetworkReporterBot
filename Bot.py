from netmiko import ConnectHandler

huawei1 = {
    'device_type': 'huawei',
    'host': '10.120.112.2',
    'username': 'unimus',
    'password': '5n3m5s_w4m',
    'port': 22  # optional
}

net_connect = ConnectHandler(**huawei1)

net_connect.enable()

list =  ['display mac-address'] #', 'display arp', 'display ip routing-table',
        #'display ip routing-table all-vpn-instance', 'display interface brief', 'display ip interface brief',
        #'display ospf peer brief', 'display ospf interface']'''

for command in list:
    output = net_connect.send_command(command)
    f = open('prueba.txt', 'w+')
    f.write(output)
    f.close()
