from interfaces.Respirar import RespiraAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Nadar import NadarAble
from interfaces.Volar import VolarAble

class Aguila(RespiraAble, TerrestreAble, NadarAble, VolarAble):

    def Respirar(self):
        print("El Aguila Respira")

    def Terrestre(self):
        print("El Aguila camina")    

    def Nadar(self):
        print("El Aguila puede nadar cuando caza")

    def Volar(self):
        print("El Aguila puede volar")