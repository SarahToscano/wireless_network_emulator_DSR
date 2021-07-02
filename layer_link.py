from layer_physical import Physical_Layer
from entity import next_send_list, show_mac_id_list
from package import Package
from random import randint
from header import Header
#from importar cores gospeis#


class Link_Layer:

    def __init__(self, Physical_Layer):
        self._backoff = 0
        self._way_access = True
        self._Physical_Layer = Physical_Layer
        self._pck_read = []

    def send_pck(self):
        self._way_access = self.way_access()

        if(self._way_access == True):  # verifica se o meio está livre
            if(self._Physical_Layer._pck_sent != []):
                if(self.backoff == 0):
                    self._Physical_Layer.send_pck()
                else:
                    next_send_list.append(self._Physical_Layer._mac)
                    self._backoff = (self._backoff - 1)
        elif(self._Physical_Layer._pck_sent != []):
            if(self._backoff == 0):
                self._backoff = randint(1, 8)
                self.show_backoff(self._Physical_Layer._mac, self._backoff)
                next_send_list.append(self._Physical_Layer._mac)

    def receive_pck(self):
        if(len(self._Physical_Layer._pck_received) > 1):
            self._Physical_Layer._pck_received.clear()
            self.print_collision(self._Physical._mac)
        else:
            if(len(self._Physical_Layer._pck_received) == 1):
                Package = self._Physical_Layer._pck_received.pop(0)
                header = Package.get_header_link()

                if(header._final_mac == self._Physical_Layer._mac):
                    self._pck_read.append(Package)
                elif(header._final_mac == -1):
                    self._pck_read.append(Package)

    def print_collision(self, mac):
        print("\rID: ", mac, "Houve Colisão")

    def way_access(self):
        if(self._Physical_Layer._pck_received == []):
            return True
        else:
            return False

    def add_pck(self, final_mac, Package):
        header = Header("Link", self._Physical_Layer._mac,
                        final_mac, 0, -1, -1, -1)
        Package.add_header(header)
        self._Physical_Layer._send_pck.append(Package)
