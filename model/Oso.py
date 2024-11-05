from interfaces.Respirar import RespiraAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Nadar import NadarAble

class Oso(RespiraAble, TerrestreAble, NadarAble):

    def Respirar(self):
        print("El Oso Respira")

    def Terrestre(self):
        print("El Oso camina")    

    def Nadar(self):
        print("El Oso puede nadar")