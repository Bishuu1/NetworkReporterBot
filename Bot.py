import os
import schedule
import time
from datetime import datetime, timedelta 
from netmiko import ConnectHandler
from maquinas import devices

def job():
    for ip in devices:  
        parent_directory_date = '/home/observium_admin/reportes'
        day_directory = datetime.today().strftime('%A')
        day_path = os.path.join(parent_directory_date,day_directory) #Directory for everyday report
        try:
            os.mkdir(day_path)
            print('the directory has been created')
        except OSError as error:
            print(error)

        parent_directory = day_path
        directory = ip['host']
        path = os.path.join(parent_directory,directory) #Directory for every machine
        try:
            os.mkdir(path)
            print('the directory has been created')
        except OSError as error:
            print(error)

        net_connect = ConnectHandler(**ip)
        net_connect.enable()


        list =  ['display version', 'display mac-address', 'display arp',
                'display interface brief', 'display ip interface brief',
                'display ospf peer brief', 'display ospf interface']

        for command in list:
            output = net_connect.send_command(command)
            f_name = "display logbuffer startime yesterday.txt" if command == logbuffer else command+'.txt'
            complete_name = os.path.join(path,f_name) #Path to create the files
            f = open(complete_name,'w+')
            f.write(output)
            f.close()
        net_connect.disconnect
    print('Reports had successfully created')



schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(30)