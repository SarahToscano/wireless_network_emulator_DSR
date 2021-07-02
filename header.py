class Header:

    def __init__(self, type_layer, mac_origem, final_mac, n, req, num_pack, seq_list):

        if(type_layer == "Link"):
            self._type_layer = "Link"
            self._mac_origem = mac_origem
            self._final_mac = final_mac
            self._n = n

        if(type_layer == "Network"):
            self._type_layer = "Network"
            self._final_mac = final_mac
            self._req = req
            self._num_pack = num_pack
            self._seq_list = seq_list
