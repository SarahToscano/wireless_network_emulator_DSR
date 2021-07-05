from layer_physical import Physical_Layer
from entity import next_send_list, show_mac_id_list
from package import Package
from random import randint
from header import Header


from colors import LINK
from colors import REDE
from colors import FISICA

class Link_Layer:

    def __init__(self, Physical_Layer):
        self._backoff = 0
        self._way_access = True
        self._Physical_Layer = Physical_Layer
        self._pck_read = []

    def send_pack(self):
        print(LINK, "LINK LAYER ACTIVATED")
        self._way_access = self.way_access()

        if(self._way_access == True):  # verifica se o meio está livre
            if(self._Physical_Layer._pck_sent != []): 
                print(LINK, "[Link Layer] - Verifying the backoff time...")
                if(self._backoff == 0):
                    print(LINK, "[Link Layer] - Not in the backoff time")
                    print(LINK, "[Link Layer] - Calling the Physical Layer to send package")
                    self._Physical_Layer.send_pack()
                else:
                    print(LINK, f"[Link Layer] - Host[{self._Physical_Layer._mac}]: Im in Backoff time")
                    next_send_list.append(self._Physical_Layer._mac)
                    self._backoff = (self._backoff - 1)
        else:
            if(self._Physical_Layer._pck_sent != []):
                if(self._backoff == 0):
                    self._backoff = randint(1, 3)
                    self.show_Backoff(self._Physical_Layer._mac, self._backoff)
                    next_send_list.append(self._Physical_Layer._mac)

    def receive_pck(self):
        print(LINK, "PACKAGE RECEIVED IN THE LINK LAYER")

        print(LINK, f'Host[{self._Physical_Layer._mac}: Origem')

        if(len(self._Physical_Layer._pck_received) > 1):
            self._Physical_Layer._pck_received.clear()
            self.print_collision(self._Physical_Layer._mac)
        else:
            if(len(self._Physical_Layer._pck_received) == 1):
                Package = self._Physical_Layer._pck_received.pop(0)
                header = Package.get_header_link()

                if(header._final_mac == self._Physical_Layer._mac):
                    self._pck_read.append(Package)
                elif(header._final_mac == -1):
                    self._pck_read.append(Package)

    def show_Backoff(self, mac, backoff):
        print("\rID: ", mac, ": Im in Backoff, value: ", backoff)

    def print_collision(self, mac):
        print('\033[31m', f"\rCollision detected Host[{mac}]")

    def way_access(self):
        print(LINK, "[Link Layer] - Verifying if the way access is free...")
        if(self._Physical_Layer._pck_received == []):
            print('\033[32m', "[Link Layer] - free access")
            return True
        else:
            print('\033[31m', "[Link Layer] - No free access")
            return False

    def add_pck(self,  Package, final_mac):
        print(LINK, "LINK LAYER ACTIVATED")
        print(LINK, "[Link Layer] - Acessing the Add_pack method")
        header = Header("Link", self._Physical_Layer._mac,
                        final_mac, 0, -1, -1, -1)
        Package.add_header(header)
        print(LINK, "[Link Layer] - Adding package to list_pack whose will be send to Physical Layer")
        self._Physical_Layer._pck_sent.append(Package)
