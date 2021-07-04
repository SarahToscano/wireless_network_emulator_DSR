from entity import mac_id_send_list
from route import Route
import random
from package import Package
from header import Header
from layer_physical import Physical_Layer
from layer_link import Link_Layer

from colors import LINK
from colors import REDE
from colors import FISICA


class Network_layer:

    def __init__(self, Link_Layer):
        self._link_layer = Link_Layer
        self._pcks_list = []
        self._RREQS_list = []
        self._wait_routes_list = []
        self._routes = []

    def RREP(self, mac_final, seq, route):
        id = self._link_layer._Physical_Layer._mac
        header = Header("Network", id, mac_final, -1, 1, -1, seq)
        pck = Package(route, 1)  # Create the package
        pck.add_header(header)  # Insert the Network Layer's header

        msg = "Sending RREP"
        self.show_package_Mac(msg, id, mac_final)

        # Define the request route
        for i, mac in enumerate(header.num_pack):
            if(mac == id):
                next_node = header.num_pack[i+1]
                next_pck = pck
                self._link_layer.add_pck(next_pck, next_node)
                break

    def RREQ(self, mac_final):
        id = self._link_layer._Physical_Layer._mac
        seq = []
        seq.append(id)  # add first ID
        seqNum = random.randint(1, 50)  # package num
        self._RREQS_list.append(seqNum)

        header = Header("Network", id, mac_final, -1, 0, seqNum, seq)
        pck = Package("", 1)  # Create the package
        pck.add_header(header)  # Insert the Network Layer's header
        msg = "Sending RREQ "

        # The dif of RREP Mac_final here is None
        self.show_package_Mac(msg, id, None)
        self._link_layer.add_pck(pck, -1)

    def show_package(self, mensagem, id, mac_final):
        print("ID: ", id, "Mensg: ", mensagem, " macDest: ", mac_final)

    def add_pck(self, mac_final, mensage, t):
        id = self._link_layer._Physical_Layer._mac
        pck = Package(mensage, t)
        header = Header("Network", id, mac_final, -1, -1, -1, None)
        print(REDE, "adding the netwok header to the package")
        pck.add_header(header)
        self._pcks_list.append(pck)  # Add package to list
        print("\033[37m", "adding the package in the package list\n")


    

    def show_package_Mac(self, mensagem,  id, mac_final):
        print("ID: ", id, "Mensg: ", mensagem, " macDest: ", mac_final)

    def show_package_Seq(self, mensagem,  id, sequenNum):
        print("ID: ", id, "Mensg: ", mensagem,
              " Numero de seq: ", sequenNum)

    def send_pack(self):
        if(self._pcks_list != []):  # is there any package?
            pck = self._pcks_list[0]
            header = pck.get_header_network()
            seq = None

            for route in self._routes:
                if(route._receiver == pck._headers[0].final_mac):
                    seq = route._seq
                    if (pck._headers[0].final_mac in self._wait_routes_list):
                        self._wait_routes_list.remove(
                            pck._headers[0].final_mac)

            # Is there this route?
            if(seq != None):
                pck.refresh_sequence(seq)
                self._pcks_list.pop(0)

                for i, mac in enumerate(pck._headers[0]._seq_list):
                    id = self._link_layer._Physical_Layer._mac
                    if(mac == id):
                        next_node = header.num_pack[i+1]
                        break
                self._link_layer.add_pck(pck, next_node)
                id = self._link_layer._Physical_Layer._mac
                mac_id_send_list.append(id)

            elif(not header._final_mac in self._wait_routes_list):

                self._wait_routes_list.append(
                    pck._headers[0]._final_mac)
                self.RREQ(pck._headers[0]._final_mac)

        # Send pckgs to link layer
        self._link_layer.send_pack()

    def receive_pck(self):
        self._link_layer.receive_pack()  # Trata pacote recebido na camada de enlace

        # Verifica se tem pacotes recebidos
        if(self._link_layer._pck_read != []):
            pckg = self._link_layer._pck_read.pop(0)
            header = pckg.get_header_network()

            # Se o pckg for recebido for de dados
            if(header._req == -1):
                id = self._link_layer._Physical_Layer._mac
                # Verifica se o pckg é para aquele host
                if(header._final_mac == id):
                    msg = "pckg de dados: "
                    self.show_package_Mac(
                        msg, id, pckg._data)
                else:
                    msg = "Chegada de pacote de dados mas não é pra mim "
                    self.show_package(
                        msg, self._link_layer._Physical_Layer._mac, 0)
                    msg_2 = "Enviando pacote de dados para o nó seguinte"
                    self.show_package(
                        msg_2, self._link_layer._Physical_Layer._mac, 0)

                    for i, mac in enumerate(pckg._headers[0]._seq_list):
                        id = self._link_layer._Physical_Layer._mac
                        if(mac == id):
                            next_node = header.num_pack[i-1]
                            break

                    pckg._headers.pop(1)
                    self._link_layer.add_pck(pckg, next_node)

                    id = self._link_layer._Physical_Layer._mac
                    mac_id_send_list.append(id)

            # Se o pacote for recebido for um RREQ
            elif(header._req == 0):
                mensage = "Chegada de pacote RREQ"
                self.show_sequence_num(
                    mensage, self._link_layer._Physical_Layer._mac, header.num_pack)
                # Verifica se esse RREQ já foi recebido pelo nó
                if(not header.num_pack in self._RREQS_list):
                    self._RREQS_list.append(header.num_pack)
                    header.seq_list.append(
                        self._link_layer._Physical_Layer._mac)

                    # Verifica se o RREQ é para o nó
                    if(header._final_mac == self._link_layer._Physical_Layer._mac):
                        mensage = "Eu sou o destino do RREQ"
                        self.show_package(
                            mensage, self._link_layer._Physical_Layer._mac, 0)
                        route = header.seq_list
                        final_mac = route[0]
                        sequence_route = route
                        sequence_route.reverse()
                        self.send_RREP(final_mac, sequence_route, route)
                        mac_id_send_list.append(
                            self._link_layer._Physical_Layer._mac)

                    else:
                        print("ID: ", self._link_layer._Physical_Layer._mac,
                              "Eu não sou o destino do RREQ")
                        self._link_layer.add_pck(pckg, -1)
                        mac_id_send_list.append(
                            self._link_layer._Physical_Layer._mac)

                else:
                    mensage = "Ja tenho esse RREQ"
                    self.show_package_Seq(
                        mensage, self._link_layer._Physical_Layer._mac, header.num_pack)
            # Se o pacote for recebido for um RREP
            elif(header._req == 1):
                dest = header._final_mac
                mensage = "Chegada de pacote RREP: "
                self.show_package_Seq(
                    mensage, self._link_layer._Physical_Layer._mac, header.seq_list)
                # Verifica se o RREP é para o nó
                if(dest == self._link_layer._Physical_Layer._mac):
                    mensage = "Eu sou o destino do RREP"
                    self.show_package(
                        mensage, self._link_layer._Physical_Layer._mac, 0)
                    mensage_2 = "Enviando dados"
                    self.show_package(
                        mensage, self._link_layer._Physical_Layer._mac, 0)
                    sequence_route = pckg._data
                    route = Route(header.seq_list[0], sequence_route)
                    self._routes.append(route)
                    mac_id_send_list.append(
                        self._link_layer._Physical_Layer._mac)

                else:
                    mensage = "Eu não sou o destino do RREP"
                    self.show_package(
                        mensage, self._link_layer._Physical_Layer._mac, 0)
                    for i, mac in enumerate(header.seq_list):
                        if(mac == self._link_layer._Physical_Layer._mac):
                            next_host = header.seq_list[i+1]
                            next_pck = pckg
                            pckg._headers.pop(1)
                            self._link_layer.add_pck(
                                next_pck, next_host)
                            mac_id_send_list.append(
                                self._link_layer._Physical_Layer._mac)
                            break
