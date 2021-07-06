import random
from layer_network import Network_layer
from layer_physical import Physical_Layer
from layer_link import Link_Layer
from header import Header
from package import Package
from globais import hosts_list, packages_list, mac_id_send_list, show_mac_id_list, next_send_list
from host import Host
import logging
from colors import LINK
from colors import REDE
from colors import FISICA
from colors import verde
from graph import *

logging.basicConfig(filename='report.log', filemode='w',
                    format=' %(levelname)s - %(message)s')


logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)

logging.info('Starting the application...')
print("\033[37m", "Starting the application...")

# Defining the hosts
h0 = Host(x=0, y=0, reach=2, mac=0, energy=10)
h1 = Host(x=1, y=0, reach=2, mac=1, energy=10)
h2 = Host(x=2, y=1, reach=2, mac=2, energy=10)
h3 = Host(x=3, y=0, reach=2, mac=3, energy=10)
h4 = Host(x=4, y=0, reach=2, mac=4, energy=10)
h5 = Host(x=5, y=3, reach=4, mac=5, energy=10)

logging.info(f'Creating {len(hosts_list)} Wireless Hosts...')
print("\033[37m", f'Creating {len(hosts_list)} Wireless Hosts...')

timemax = 30
for i in range(timemax):
    print("\033[35m", "\n TIME: ", i, end="\n\n", )
    print("\033[34m", 'LOOP - defining the packages')

    if(i == 0):
        hosts_list[0].create_packge(0, 2, "msg 1 - hi there!")
        mac_id_send_list.append(
            hosts_list[0]._layer_network._link_layer._Physical_Layer._mac)

    print("\033[31m", "next_send_list: ", next_send_list)
    if(next_send_list != []):
        for k in next_send_list:
            mac_id_send_list.append(k)
    del next_send_list[:]

    # Existe algum nó querendo receber, recebe
    print("\033[31m", "show_mac_id_list: ", show_mac_id_list)
    for k in show_mac_id_list:
        hosts_list[k]._layer_network.receive_pck()
    del show_mac_id_list[:]

    # Existe algum nó querendo transmitir, transmite naquele instante se posssível
    print("\033[31m", "List of hosts that will send: ", mac_id_send_list)
    for k in mac_id_send_list:
        print(
            verde, f"[main] - host[{hosts_list[k]._mac}] Preparing to send the package to Network Layer")
        hosts_list[k]._layer_network.send_pack(i)
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

plot_graph(hosts_list, -10, -10, 10, 10)
