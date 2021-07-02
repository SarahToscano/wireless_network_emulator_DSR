from entity import mac_id_send_list
from route import Route
import random
from package import Package
from header import Header
from layer_physical import Physical_Layer
from layer_link import Link_Layer

class Network_layer:

    def __init__(self, layer_link):
            self._link_layer = layer_link
            self._pcks_list = []
            self._RREQS_list = []
            self._wait_routes_list = []
            self._routes = []
    
    def RREP(self, mac_final, seq, route):
        id = self._layer_link._layer_physical._mac
        header = Header("Network", id, mac_final, -1, 1, -1, seq)
        pck = Package(route, 1) #Create the package
        pck.add_header(header) #Insert the Network Layer's header

        msg = "Sending RREP"
        self.show_package_Mac(msg, id, mac_final)

        # Define the request route
        for i, mac in enumerate(header.seq_list):
            if(mac == id):
                next_node = header.seq_list[i+1]
                next_pck = pck
                self._layer_link.add_pck(next_pck, next_node)
                break

    def RREQ(self, mac_final):
        id = self._layer_link._layer_physical._mac
        seq = []
        seq.append(id) #add first ID
        seqNum = random.randint(1, 50) #package num
        self._RREQS_list.append(seqNum)

        header = Header("Network", id, mac_final, -1, 0, seqNum, seq)
        pck = Package("", 1) #Create the package
        pck.add_header(header) #Insert the Network Layer's header
        msg = "Sending RREQ "

        self.show_package_Mac(msg, id, None) # The dif of RREP Mac_final here is None
        self._link_layer.add_pck(pck, -1)

    def add_pck(self, mac_final, mensage, t):
        id = self._camadaEnlace._camadaFisica._mac
        pck = Package(mensage, t)
        header = Header("REDE", id, mac_final, -1, -1, -1, None)
        pck.add_header(header)
        self._pcks_list.append(pck) #Add package to list


    def show_package(self, mensagem, id, mac_final):
        print("ID: ", id, "Mensg: ", mensagem, " macDest: ", mac_final)

    def show_package_Mac(self, mensagem,  id, mac_final):
        print("ID: ", id, "Mensg: ", mensagem, " macDest: ", mac_final)

    def show_package_Seq(self, mensagem,  id, sequenNum):
        print("ID: ", id, "Mensg: ", mensagem,
              " Numero de seq: ", sequenNum)
