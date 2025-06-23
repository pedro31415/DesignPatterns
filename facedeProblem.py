# facade
class VendaFacede:
    def __init__(self):
        self.estoque = Estoque()
        self.pagamento = Pagamento()
        self.nota_fiscal = NotaFiscal()
        self.entrega = Entrega()
    
    def realizar_venda(self, produto, quantidade, tipo_pagamento, valor):
        self.estoque.verficar_produto(produto)
        self.estoque.baixa_estoque(quantidade)

        self.pagamento.validar_pagamento(valor)
        self.pagamento.processar_pagamento(tipo_pagamento)

        self.nota_fiscal.gera_nota()
        self.nota_fiscal.enviar_nota()

        self.entrega.agendar_entrega()
        self.entrega.gerar_codigo()

        print("Venda concluida")
        



# subSistema
class Estoque:
    def verficar_produto(self, produto):
        print(f"O produto {produto} está disponivel")
    
    def baixa_estoque(self, quantidade):
        print(f"Temos {quantidade} no estoque")

class Pagamento:
    def processar_pagamento(self, tipo):
        print("pagamento com ", tipo)
    
    def validar_pagamento(self, valor):
        print(f"Valor {valor} fornecido e correto")

class NotaFiscal:
    def gera_nota(self):
        print("Nota fiscal gerada com sucesso")

    def enviar_nota(self):
        print("Nota fiscal enviada com sucesso para o cliente")

class Entrega:
    def agendar_entrega(self):
        print("Agendamento concluido com sucesso")
    
    def gerar_codigo(self):
        print("Codigo gerado com sucesso")


if __name__ == "__main__":
    facade = VendaFacede()
    facade.realizar_venda(
        produto="Notebook Gamer",
        quantidade=2,
        tipo_pagamento="Cartão de crédito",
        valor=7500.00
    )