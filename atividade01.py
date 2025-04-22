# Em um sistema de vendas é desejável suporte a vários regras para cálculo de imposto:
# Imposto para EUA (Algoritmo que calcula o imposto no EUA);
# Imposto para Brasil (Algoritmo que calcula o imposto no Brasil);
# Imposto para Canada (Algoritmo que calcula o imposto no Canada);
# Desenvolva uma aplicação simples que usa o padrão Strategy como solução ao requisito proposto

from abc import ABC, abstractmethod

class ImpostoStrategy(ABC):
    @abstractmethod
    def imposto(self):
        pass

class PedidoVenda():
    def impostoVenda(self, valorImposto: ImpostoStrategy):
        return  valorImposto.imposto()

class ImpostoEUA(ImpostoStrategy):
    def imposto(self, valor):
        return 0.10  * valor
    
class ImpostoBrasil(ImpostoStrategy):
    def imposto(self, valor):
        return 0.21 * valor

class ImpostoCanada(ImpostoStrategy):
    def imposto(self, valor):
        return 0.05 * valor

if __name__ == "__main__":
    valor = PedidoVenda()
    imposto = valor.impostoVenda(ImpostoBrasil())
    print(imposto)