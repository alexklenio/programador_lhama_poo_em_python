class Pessoa:
    def __init__(self,nome, altura,idade):
        self.nome = nome
        self.saltura = altura
        self.idade = idade

    def correr(self):
        print(f"{self.nome} está correndo!")

    def comer(self):
        print(f"{self.nome} está comendo.")

    def apresentar(self):
        print(f"Nome: {self.nome}\nAltura: {self.saltura}\nIdade: {self.idade}")


pessoa_1 = Pessoa("Alex", 1.83, 39)
pessoa_1.correr()