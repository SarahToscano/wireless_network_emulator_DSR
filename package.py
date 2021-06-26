import logging

class package:
	def __init__(self, id, type, origem, ID, mensage):
		self.id = id
		self.type = type
		self.route = []
		self.next = 0
		self.mensage = mensage
		self.origem = origem
		self.ID = ID
		
	def add_route(self, host):
		if(self.type == 'RREQ' or self.type == 'RREP'):
			self.route.append(host)    
			aux = getattr(host,'mac')
			logging.info(f'Adding host[{aux}] to the route list')

	def set_next_mac(self, next_mac):
		if(self.type == 'RREQ' or self.type == 'RREP'):
			self.next.append(next_mac)
			print(f'The next host will be [{next_mac}')

	

	

         



