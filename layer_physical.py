from neighbors import neighbors
from package import Package
from entity import hosts_list
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
        show_mac_id_list.append(self._id)  # Global List
        self._pck_received.append(package)  # Add package to received list

    def find_neighbors(self):
        self._energy -= 1  # drain battery
        print("energy:", self._energy)
        nodes = len(hosts_list)
        for i in range(0, nodes):
            if(hosts_list[i]._mac != self._mac):
                if(neighbors(self._x, self._y, self._reach, hosts_list[i]._x, hosts_list[i]._y)):
                    if(hosts_list[i] not in self._neighborhood):
                        self._neighborhood.append(hosts_list[i])

    def send_pck(self, package):
        self.find_neighbors()
        self._pck_sent.append(package)
        print(package, self._pck_sent, self._pck_sent[0],"teste")
        for host in self._neighborhood:
            # Send packages to their neighborhood
            host.link_layer.receive_pck()
        # Add package to save list
        self._pck_saves.append(self._pck_sent.pop(0))
