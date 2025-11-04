from abc import ABC,abstractmethod

class Trabalhador(ABC): #Interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoço(self) -> None: pass


class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print(f"O professor está dando aula.")

    def ir_para_casa(self) -> None:
        print(f"O professor está indo para casa.")

    def horario_de_almoço(self) -> None:
        print(f"O professor está almoçando.")

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print(f"O Engenheiro está trabalhando.")

    def ir_para_casa(self) -> None:
        print(f"O Engenheiro está indo para casa.")

    def horario_de_almoço(self) -> None:
        print(f"O Engenheiro está almoçando.")


def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print(f"Comunicar o trabalhador para ir para casa ")
    trabalhador.ir_para_casa()

p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
print()
comunicar_o_trabalhador(p2)