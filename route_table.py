import logging

class route_table :
	def __init__(self,host):
		self.host = host
		self.route = {host.mac()}
		
	def save_route(self, path, ID):
		self.route[ID] = self.route 
	
	def next_jump(self, mac, host):
		next_jp = 0
		njp =0
		for key in self.route:
			for i in key:
				if mac == i.get_mac():
					next_jp = key
					break
		try:
			njp = next_jp.index(host)+1
		except :
			return False

		njp = next_jp[njp]
		return njp.get_mac() # return the next jump point