import logging

def physical_send(reach_list, origem, mensage, hosts_list):
    nodes = len(reach_list)
    logging.warning('Physical Layer activated')

    for i in range (0, nodes):
        logging.info(f'Sending package: Host[{origem}] -> Host[{reach_list[i]}]')
        '''for k in range (0, len(mensage)):
            hosts_list[reach_list[i]].pckg.append(mensage[k]);
            print('\t\t\t', hosts_list[reach_list[i]].pckg[k] )
        '''
def physical_receive(reach_list, origem, mensage):
    nodes = len(reach_list)
    logging.warning('Physical Layer activated')

    for i in range (0, nodes):
        logging.info(f'Sending mensage: Host[{origem}] -> Host[{reach_list[i]}]')

