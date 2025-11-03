class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:
        print(f"Estou acendendo a luz do comodo: {self.comodo}")

    def apagar(self) -> None:
        print(f"Estou apagando a luz do comodo: {self.comodo}")


class Pessoa:
    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print("A pessoa foi dormir")


alex = Pessoa()
interruptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")


alex.acender_luzes(interruptor_sala)
alex.apagar_luzes(interruptor_sala)
