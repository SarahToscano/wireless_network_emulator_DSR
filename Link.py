import logging
import controller

class link_layer:

    def __init__(self, host):
        self.host = host
        self.hanging_packages = []
        self.packages = 0

    '''
        # check if the dict has key "host"
	def check_route(self, host):
		if host in self.route:
			return True
		else:
			return False
    '''


    def receive_package_from_physical(self, package):
        self.host.network.receive_package(package)

    def send_request_to_host(self, package):
        self.hanging_packages.append(package)
        print(f'L2: List of packages in link_layer :{self.hanging_packages}')
        #adicionar um log aqui
        self.host.master.add_queue(self.host)
        #fazer classe master para fila de requições e afins

    '''def send_package_to_physical(self):
        self.packages = self.hanging_packages.pop(0)
	 	#print(f'L2: Link_Layer [{self.host.get_mac()}]')
	 	self.packages.packages_info()
	 	self.host.physical.send_package(self.packages)
    '''