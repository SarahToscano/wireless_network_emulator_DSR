import math
import logging

def physical(reach_list, origem, mensage):
    nodes = len(reach_list)
    logging.warning('Physical Layer activated')

    for i in range (0, nodes):
        logging.info(f'Sending mensage: Host[{origem}] -> Host[{reach_list[i]}]')

