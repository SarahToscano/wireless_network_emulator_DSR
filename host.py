from physical_layer import physical
from neighbors import neighbors

class host:
    def __init__(self, x, y, reach, mac):	#delfaut constructor
        self.posX = x
        self.posY = y
        self.reach = reach
        self.mac = mac   
    
    def sender(self, mensage, ID, hosts_list):	#delfaut constructor
        self.sender_id = self.mac
        self.mensage = mensage
        self.ID = ID
        neighboorhood= neighbors(hosts_list, self.sender_id)
        physical(neighboorhood, self.sender_id, mensage)





    #Getter Method
    def get_posX(self):
        return self.posX
    def get_posY(self):
        return self.posY
    def get_ID(self):
        return self.ID
    def get_reach(self):
        return self.reach
    def get_mac(self):
        return self.mac
    
    #Getter Method
    def get_sender_id(self):
        return self.sender_id
    def get_message(self):
        return self.message
    def get_ID(self):
        return self.ID

        