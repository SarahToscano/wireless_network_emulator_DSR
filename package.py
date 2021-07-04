import logging
#from header import Header


class Package:

    def __init__(self, mensage, t):
        self._id = -1
        self._data = mensage
        self._t = t
        self._headers = []

    @staticmethod
    def create_pck(mensage, t):
        print("Creating a Package")
        return Package(mensage, t)

    def get_header_network(self):
        for header in self._headers:
            print(f"Reading the package network header -> ID:", header._id)
            if(header._layer == "Network"):
                return header

    def get_header_link(self):
        for header in self._headers:
            print("Reading the package Link header", header._layer, "-> ID:", header._id)
            if(header._layer == "Link"):
                return header

    def add_header(self, header):
        print("\033[34m", f"Adding the {header._layer} header in the pack")
        self._headers.append(header)

    def show_pck_info(self):
        print("Dados: ", self._data)

    def refresh_sequence(self, sequence):
        for header in self._headers:
            if (header._layer == "Network"):
                header._seq_list = sequence
