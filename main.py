from host import host
from physical_layer import physical_send
import logging
from controller import requests_n

logging.getLogger().setLevel(logging.INFO)
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%I:%M:%S')

logging.info('Starting the application...')

#Defining the hosts
n_hosts = 4
logging.info(f'Creating {n_hosts} Wireless Hosts...')
h0 = host (x=1, y=0, reach=4, mac=0, pckg =[])
h1 = host (x=2, y=3, reach=4, mac=1, pckg =[])
h2 = host (x=3, y=5, reach=4, mac=2, pckg =[])
h3 = host (x=6, y=8, reach=4, mac=3, pckg =[])
h4 = host (x=5, y=7, reach=4, mac=4, pckg =[])

hosts_list = [h0, h1,h2,h3,h4]
sender_list = [h1,h3]
h1.sender(mensage=["m1", "m2", "m3"], ID=4)
h3.sender(mensage=["m6"], ID=0)

req = requests_n(sender_list, hosts_list)
logging.warning(f'{req} mensage requests')


