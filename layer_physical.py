from neighbors import neighbors
from package import Package
from entity import hosts_list
from entity import show_mac_id_list


from colors import LINK
from colors import REDE
from colors import FISICA

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
        print(FISICA, "PACKAGE RECEIVED IN PHYSICAL LAYER")

        show_mac_id_list.append(self._mac)  # Global List
        self._pck_received.append(package)  # Add package to received list

    def find_neighbors(self):
        print(FISICA, f'Find Neighbors of host [{self._mac}]...')
        self._energy -= 1  # drain battery
        print("energy:", self._energy)
        nodes = len(hosts_list)
        for i in range(0, nodes):
            if(hosts_list[i]._mac != self._mac):
                if(neighbors(self._x, self._y, self._reach, hosts_list[i]._x, hosts_list[i]._y)):
                    if(hosts_list[i] not in self._neighborhood):
                        print("\033[31m",f"Found Host[{hosts_list[i]._mac}]")
                        self._neighborhood.append(hosts_list[i])

    def send_pack(self, package):
        print(FISICA, "Physical Layer Activated")
        self.find_neighbors()
        self._pck_sent.append(package)
        #print(package, self._pck_sent, self._pck_sent[0],"teste")
        for host in self._neighborhood:
            print(FISICA, "Send packages to their neighborhood")
            host._layer_network._link_layer._Physical_Layer.receive_pck(self._pck_sent[0])
        # Add package to save list
        print(FISICA, "Adding the pack in the save list")
        self._pck_saves.append(self._pck_sent.pop(0))
