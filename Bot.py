from netmiko import ConnectHandler

huawei1 = {
    'device_type': '',
    'host': '',
    'username': '',
    'password': '',
    'port':   # optional
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
