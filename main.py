import random
from layer_network import Network_layer
from layer_physical import Physical_Layer
from layer_link import Link_Layer
from header import Header
from package import Package
from entity import hosts_list, packages_list, mac_id_send_list, show_mac_id_list, next_send_list
from host import Host
import logging

logging.basicConfig(filename='report.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%I:%M:%S')

logging.info('Starting the application...')

# Defining the hosts
n_hosts = 5
logging.info(f'Creating {n_hosts} Wireless Hosts...')
h0 = Host(x=0, y=0, reach=2, mac=0, energy=10)
h1 = Host(x=1, y=0, reach=2, mac=1, energy=10)
h2 = Host(x=2, y=1, reach=2, mac=2, energy=10)
h3 = Host(x=3, y=0, reach=2, mac=3, energy=10)
h4 = Host(x=4, y=0, reach=2, mac=4, energy=10)
h5 = Host(x=5, y=3, reach=4, mac=5, energy=10)

hosts_list = [h0, h1, h2, h3, h4, h5]

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

# Loop do tempo
for i in range(30):
    print("\n Tempo: ", i, end="\n\n", )
    # Loop para percorrer
    for host in hosts_list:
        # Numero aleatorio entre 0 e 100 para probabilidade de criação de pacotes
        rand = random.randint(0, 100)
        # Numero aleatorio entre 0 e a quantidade de hosts, para escolher um para enviar
        send = random.randint(0, len(hosts_list)-1)
        # Teste se rand é menor que 4
        if(rand < 3):
            # Se o ID do destino for diferente do dele mesmo, adiciona o pacote no host
            if(send != (host._layer_network._link_layer._Physical_Layer._mac)):
                host.create_packge(1, 3, "Será que vamos passar")
                mac_id_send_list.append(
                    host._layer_network._link_layer._Physical_Layer._mac)

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
