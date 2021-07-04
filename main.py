import random
from layer_network import Network_layer
from layer_physical import Physical_Layer
from layer_link import Link_Layer
from header import Header
from package import Package
from entity import hosts_list, packages_list, mac_id_send_list, show_mac_id_list, next_send_list
from host import Host
import logging
from colors import LINK
from colors import REDE
from colors import FISICA

logging.basicConfig(filename='report.log', filemode='w',
                    format=' %(levelname)s - %(message)s')


logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)

logging.info('Starting the application...')
print("\033[37m","Starting the application...")

# Defining the hosts
h0 = Host(x=0, y=0, reach=2, mac=0, energy=10)
h1 = Host(x=1, y=0, reach=2, mac=1, energy=10)
h2 = Host(x=2, y=1, reach=2, mac=2, energy=10)
h3 = Host(x=3, y=0, reach=2, mac=3, energy=10)
h4 = Host(x=4, y=0, reach=2, mac=4, energy=10)
h5 = Host(x=5, y=3, reach=4, mac=5, energy=10)

logging.info(f'Creating {len(hosts_list)} Wireless Hosts...')
print("\033[37m",f'Creating {len(hosts_list)} Wireless Hosts...')

timemax = 5 
for i in range(timemax):
    print("\033[35m", "\n TIME: ", i, end="\n\n", )
    logging.info(f"\n TIME: {i}")


    #Create all packages
    print("\033[34m", 'LOOP - defining the packages')
    for host in hosts_list:
        print("\033[34m",f'Origem: Host[{host._mac}]')
        destinationHost = random.randint(0, len(hosts_list)-1)
        print("\033[34m",f'Destination: Host[{destinationHost}]')
        prob = random.randint(0, 10)
        if(prob > 7):
            #o mac o host que quer enviar é != o que vai receber?
            if(host._layer_network._link_layer._Physical_Layer._mac != destinationHost):
                print("\033[32m",'Package? YEEEESS!!!\n')

                host.create_packge(i, destinationHost, "msg 1 - testeeeeeeeeeeee")
                mac_id_send_list.append(
                    host._layer_network._link_layer._Physical_Layer._mac)

            else:
                print("\033[31m", 'Package? NO!!! Same ID and Final Mac ;(')
            
        else:
            print("\033[31m", 'Package? NO!!!')


    if(next_send_list != []):
        for i in next_send_list:
            mac_id_send_list.append(i)
    del next_send_list[:]

    # Existe algum nó querendo receber, recebe
    for j in show_mac_id_list:
        hosts_list[j]._layer_network.receive_pack()
    del show_mac_id_list[:]

    # Existe algum nó querendo transmitir, transmite naquele instante se posssível
    for i in mac_id_send_list:
        hosts_list[i]._layer_network.send_pack()
    del mac_id_send_list[:]

    

    mac = []
    x = []
    y = []
    reach = []

    for host in hosts_list:
        mac.append(host._layer_network._link_layer._Physical_Layer._mac)
        x.append(host._layer_network._link_layer._Physical_Layer._x)
        y.append(host._layer_network._link_layer._Physical_Layer._y)
        reach.append(host._layer_network._link_layer._Physical_Layer._reach)


    #criaGraficos(id, x, y, reach)
