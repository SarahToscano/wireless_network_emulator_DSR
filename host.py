from neighbors import neighbors
import logging
from entity import hosts_list
from layer_network import Network_layer
from layer_physical import Physical_Layer
from layer_link import Link_Layer

from colors import LINK
from colors import REDE
from colors import FISICA
from colors import ciano


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
        print(ciano,'\n[Host class] - Create Package method of host class -> Creating a package')
        self.show_package(
            self._layer_network._link_layer._Physical_Layer._mac, final_mac, mensage)

        print(ciano,'[Host class] - Preparing to add  the package in the layer network...')   
        self._layer_network.add_pck(final_mac, mensage, t)

    def show_package(self,  id, final_mac, mensage):
        print(f"Host[{id}]-> Host[{final_mac}]: mensage -> {mensage}")

    def drain_energy(self):
        print("Host Energy:", self._energy)
