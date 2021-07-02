from host import host
from physical_layer import physical
import logging

logging.basicConfig(filename='report.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%I:%M:%S')

logging.info('Starting the application...')

#Defining the hosts
n_hosts = 5
logging.info(f'Creating {n_hosts} Wireless Hosts...')
h0 = host (x=1, y=0, reach=4, mac=0)
h1 = host (x=2, y=3, reach=4, mac=1)
h2 = host (x=3, y=5, reach=4, mac=2)
h3 = host (x=6, y=8, reach=4, mac=3)
h4 = host (x=5, y=7, reach=4, mac=4)

hosts_list = [h0, h1,h2,h3,h4]
sender_list = [h1,h3]
h1.sender(mensage=["m1", "m2", "m3"], ID=4)
h3.sender(mensage=["m6"], ID=0)

for i in range (0, len(sender_list)):
    #req = host.requests_n(sender_list[i], hosts_list)
    req = physical.physical_send(sender_list[i], hosts_list)

logging.warning(f'{req} mensage requests')


