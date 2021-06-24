from host import host
from neighbors import neighbors
import logging

logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%I:%M:%S')

logging.info('Starting the application...')

#Defining the hosts
n_hosts = 4
logging.info(f'Creating {n_hosts} Wireless Hosts...')

h0 = host (x=1, y=0, reach=4, mac=0)
h1 = host (x=2, y=3, reach=4, mac=1)
h2 = host (x=3, y=5, reach=4, mac=2)
h3 = host (x=6, y=8, reach=4, mac=3)
h4 = host (x=5, y=7, reach=4, mac=4)
host_list = [h0, h1,h2,h3,h4]

#Sending mensage
logging.info(f'Trying to send a message: Host[1] - Host[4]')
h1.sender(message="teste", ID=4)

neighbors(host_list, h1.mac)
