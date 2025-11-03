class Loja:
    taxa = 1.15

    def __init__(self, valor: float) -> None:
        self.valor_produto_bruto = valor

    def consultar_valor_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f"valor doproduto: {valor_produto}")

    @classmethod
    def editar_taxa_produto(cls, valor: float):
        cls.taxa = valor
