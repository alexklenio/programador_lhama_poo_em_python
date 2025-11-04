class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self)-> None:
        print(f"O animal está andando pelo {self.localizacao}")

    def _dormir(self) -> None:
        print(f"O animal está dormindo")

class Gato(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)

    def miar(self) -> None:
        print(f"O {__class__.__name__} está miando")
        self._dormir()

cat = Gato("Argentina")
cat.miar()