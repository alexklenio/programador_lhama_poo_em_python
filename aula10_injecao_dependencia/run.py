class Celular:
    def __init__ (self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem:str) -> None:
        print(f"enviando mensagem: {mensagem}")

    def abrir_email(self) -> None:
        print("Abrindo os Emails...")

    def abrir_youtube(self) -> None:
        print ("Abrindo o YouTube...")

class Pessoa:
    def __init__ (self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("definindo o sabor...")
        self.__celular.enviar_mensagem("quero uma de calabreza")
        print("aguardando a chegada")

    def estudar(self) -> None:
        print("Pegando o celular...")
        self.__celular.abrir_youtube()
        print("Anotando o conteúdo!")

ios = Celular("iphone")
alex = Pessoa(ios)

alex.pedir_pizza()