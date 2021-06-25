import math
import logging

def neighbors(host_list, origem):
	logging.info(f'-> Finding the neighborhood of Host[{origem}] ')
	neighborhood=[]
	size = len(host_list)
	reach = (getattr(host_list[origem],'reach'))
	for i in range(0, size):
		if(i!=origem):
			#logging.info('loading...')
			a = ((getattr(host_list[origem],'posX')) - (getattr(host_list[i],'posX')))**2
			b = ((getattr(host_list[origem],'posY')) - (getattr(host_list[i],'posY')))**2
			distance = math.sqrt(a + b)
			if(distance<=(getattr(host_list[origem],'reach'))):
				neighborhood.append((getattr(host_list[i],'mac')))
	logging.info(f'Hosts reachable by Host[{origem}] : {neighborhood}')
	return neighborhood