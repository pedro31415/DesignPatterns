class PagamentoBoletoAntigo:
    def paga_com_boleto(self, valor):
        print(f"pagando {valor} com Sistema Antigo")

class PagaamentoAdapter:
    def __init__(self, sistema_antigo: PagamentoBoletoAntigo):
        self.sistema_antigo = sistema_antigo

    def realizar_pagamento(self, valor):
        self.sistema_antigo.paga_com_boleto(valor)

if __name__ == "__main__":
    
    sistema_antigo = PagamentoBoletoAntigo()
    adapter = PagaamentoAdapter(sistema_antigo)

    adapter.realizar_pagamento(100.0)