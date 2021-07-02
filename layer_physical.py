from neighbors import neighbors
from package import Package
from entity import hosts
from entity import show_mac_id_list

class Physical_Layer:

    def __init__(self, x, y, mac, reach, energy):
        self._x = x
        self._y = y
        self._mac = mac
        self._neighborhood = []
        self._pck_sent = []
        self._pck_received = []
        self._pck_saves = []
        self._reach = reach
        self._energy = energy
        
    def receive_pck(self, package):
        show_mac_id_list.append(self._id)  #Global List
        self._pck_received.append(package) #Add package to received list

    def find_neighbors(self):
        self._energy -= 1 #drain battery
        print("energy:", self._energy)
        nodes = len(hosts)
        for i in range (0, nodes):
            if(hosts[i]._mac != self._mac):
                if(neighbors(self._x, self._y, self._reach, hosts[i]._x, hosts[i]._y)):
                    if(hosts[i] not in self._neighborhood):
                        self._neighborhood.append(hosts[i])

    def send_pck(self):
        self.find_neighbors()
        for host in self._neighborhood:
            host.receive_pck(self._pck_sent[0]) # Send packages to their neighborhood
        self._pck_saves.append(self._pck_sent.pop(0)) # Add package to save list


    

 