from interfaces.Respirar import RespiraAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Nadar import NadarAble

class Gato(RespiraAble, TerrestreAble, NadarAble):

    def Respirar(self):
        print("El Gato Respira")

    def Terrestre(self):
        print("El Gato camina")    

    def Nadar(self):
        print("El Gato puede nadar")