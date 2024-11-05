from model.Aguila import Aguila
from model.Gato import Gato
from model.Oso import Oso

def main():
    animal = input("Ingrese el nombre de un animal (aguila, gato, oso): ").strip().lower()

    if animal == "aguila":
        aguila = Aguila()
        aguila.Respirar()
        aguila.Volar()
    elif animal == "gato":
        gato = Gato()
        gato.Respirar()
        gato.Terrestre()
    elif animal == "oso":
        oso = Oso()
        oso.Respirar()
        oso.Terrestre()
        oso.Nadar()
    else:
        print("Animal no reconocido")

if __name__ == "__main__":
    main()