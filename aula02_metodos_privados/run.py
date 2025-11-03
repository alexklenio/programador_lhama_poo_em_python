class Pessoa:
    def __init__ (self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def __coletar_documento(self):
        print(f"Meu documento - {self.__cpf}")

    def apresentar(self):
        print(f"Olá! Minha altura - {self.altura}")
        self.__coletar_documento()


alex = Pessoa("1.83", "07072542485")
alex.apresentar()