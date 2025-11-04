class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
    def andar(self)-> None:
        print(f"O animal está andando pelo {self.localizacao}")


class Cachorro(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def latir(self) -> None:
        print(f"O {__class__.__name__} está latindo")

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print(f"O {__class__.__name__} está miando")

rex = Cachorro("Chile")
rex.latir()
rex.andar()
print()
miau = Gato("Egito")
miau.miar()
miau.andar()