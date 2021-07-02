from neighbors import neighbors
import logging 
from entity import hosts_list

class Host:
    def __init__(self, mac, reach, x, y, energy):	#delfaut constructor
        self.posX = x
        self.posY = y
        self.reach = reach
        self.mac = mac 
        hosts_list.append(self)

        '''self._camadaRede = CamadaRede(CamadaEnlace(
            CamadaFisica(x, y, id, cobertura, bateria)))
        '''

    def create_packge(self, t, final_mac, mensage):
        self._network.add_pck(final_mac, mensage, t)
        self.show_pck(
            self._network._link._physical._id, final_mac, mensage)

    def show_package(self, final_mac, id, mensage):
        print(f"Host[{id}]-> Host[{final_mac}]: mensage -> {mensage}")

    def drain_energy(self):
        print("Host Energy:", self._energy)

'''
    def sender(self, mensage, ID):	#delfaut constructor
        self.mensage = mensage
        self.ID = ID

   
  
   

'''