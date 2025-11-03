class ClasseQualquer:
    def fazer(self) -> None:
        print("Estou fazendo algo")

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Estou preparando algo")

    def fazer(self) -> None:
        print("estou fazendo outra coisa")


obj1 = ClasseQualquer()
obj2 = OutraCoisa()

obj1.fazer()
obj2.fazer()