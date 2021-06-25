from physical_layer import physical
from neighbors import neighbors
from controller import requests_n

class host:
    def __init__(self, x, y, reach, mac):	#delfaut constructor
        self.posX = x
        self.posY = y
        self.reach = reach
        self.mac = mac 

    def sender(self, mensage, ID):	#delfaut constructor
        self.mensage = mensage
        self.ID = ID
  
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

        