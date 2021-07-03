from neighbors import neighbors
import logging
from entity import hosts_list
from layer_network import Network_layer
from layer_physical import Physical_Layer
from layer_link import Link_Layer


class Host:
    def __init__(self, mac, reach, x, y, energy):  # delfaut constructor
        self._x = x
        self._y = y
        self._reach = reach
        self._mac = mac
        hosts_list.append(self)
        self._layer_network = Network_layer(Link_Layer(
            Physical_Layer(x, y, mac, reach, energy)))

    def create_packge(self, t, final_mac, mensage):
        self._layer_network.add_pck(final_mac, mensage, t)
        self.show_package(
            self._layer_network._link_layer._Physical_Layer._mac, final_mac, mensage)

    def show_package(self, final_mac, id, mensage):
        print(f"Host[{id}]-> Host[{final_mac}]: mensage -> {mensage}")

    def drain_energy(self):
        print("Host Energy:", self._energy)
