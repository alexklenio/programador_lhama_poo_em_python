class ConnectionDB:
    def conectar(self):
        print("COnectando ap banco")

class SqlRepository(ConnectionDB):
    def selcect(self):
        print("Buscando dados no banco SQL")

class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Vuscando dados no banco NoSQL")

class DBHandler(NoSQLRepository):
    def alterTable(self):
        print("alterando tablea em SQL")

    def select(self): #QUEBRA DO PRINCIPIO DE LISKOV
        raise Exception("Não busca dados no banco NoSQL")