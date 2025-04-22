# Em um sistema de vendas é desejável suporte a vários regras para cálculo de imposto:
# Imposto para EUA (Algoritmo que calcula o imposto no EUA);
# Imposto para Brasil (Algoritmo que calcula o imposto no Brasil);
# Imposto para Canada (Algoritmo que calcula o imposto no Canada);
# Desenvolva uma aplicação simples que usa o padrão Strategy como solução ao requisito proposto

from abc import ABC, abstractmethod

class ImpostoStrategy(ABC):
    @abstractmethod
    def imposto(self, valor):
        pass

class PedidoVenda():
    def __init__(self, valor):
        self.valor = valor

    def calcularImposto(self, estrategia: ImpostoStrategy):
        return  estrategia.imposto(self.valor)

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
    valor = PedidoVenda(100)
    imposto = valor.calcularImposto(ImpostoBrasil())
    print(imposto)