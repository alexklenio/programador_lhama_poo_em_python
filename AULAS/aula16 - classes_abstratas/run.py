from abc import ABC, abstractmethod 

class Pessoa(ABC):
    def correr(self) -> None:
        print("A pessoa está correndo de manha")

    @abstractmethod
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("O professor está dando aula")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O cozinheiro está cozinhando")

p1 = Professor()
p1.trabalhar()
p1.correr()