class Header:

    def __init__(self, layer, mac_origem, final_mac, n, req, num_pack, seq_list):

        self._id = 1 
        self._layer = ""
        self._mac_origem = -1
        self._final_mac = -1
        self._n = -1
        self._num_pack = []
        self._req = -1
        self._seq_list = []

        if(layer == "Link"):
            self._layer = "Link"
            self._mac_origem = mac_origem
            self._final_mac = final_mac
            self._n = n

        if(layer == "Network"):
            self._layer = "Network"
            self._final_mac = final_mac
            self._req = req
            self._num_pack = num_pack
            self._seq_list = seq_list
