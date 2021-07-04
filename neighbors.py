import math
import logging


def neighbors(posX_origem, posY_origem, reach, posX_f, posY_f):
    a = (posX_origem - posX_f)**2
    b = (posY_origem - posY_f)**2
    euclidean = math.sqrt(a + b)
    if(euclidean <= reach):
        return True
    else:
        return False
