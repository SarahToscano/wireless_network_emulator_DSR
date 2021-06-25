import logging
from neighbors import neighbors



def find_neighboorhood(hosts_list, origem):
    neighboorhood= neighbors(hosts_list, origem)
    #physical(neighboorhood, self.mac, self.mensage)

def requests_n(senders_list, hosts_list): 
    count = 0
    for i in range (0, len(senders_list)):
        m = len(senders_list[i].mensage)
        count += m
        logging.warning(f'{m} mensages: Host[{senders_list[i].mac}] -> Host[{senders_list[i].ID}]')
        find_neighboorhood(hosts_list, senders_list[i].mac)
    return count

