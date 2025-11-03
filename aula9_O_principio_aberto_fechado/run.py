class Artista:
    def __init__ (self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando seu show!")

class Circo:
    def apresentar(self, artista:Artista) -> None:
        print("O circo está abrindo!")
        artista.apresentar_show()
        print("O público aplaude!")


circo = Circo()
palhaco = Artista("palhaco")
magico = Artista("magico")
malabarista = Artista("malabarista")

circo.apresentar(malabarista)