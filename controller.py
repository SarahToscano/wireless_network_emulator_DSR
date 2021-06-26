import logging
from neighbors import neighbors
from physical_layer import physical_send
from physical_layer import physical_receive

def find_neighboorhood(hosts_list, origem):
    return neighbors(hosts_list, origem)

def requests_n(senders_list, hosts_list): 
    count = 0
    for i in range (0, len(senders_list)):
        m = len(senders_list[i].mensage)
        count += m
        logging.warning(f'{m} mensages: Host[{senders_list[i].mac}] -> Host[{senders_list[i].ID}]')
        neighboorhood = find_neighboorhood(hosts_list, senders_list[i].mac)
        physical_send(neighboorhood, senders_list[i].mac, senders_list[i].mensage, hosts_list)

    return count

