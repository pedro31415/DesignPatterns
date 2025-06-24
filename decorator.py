from abc import ABC, abstractmethod
from datetime import datetime

# Componente base
class Mensagem(ABC):
    @abstractmethod
    def enviar(self) -> str:
        pass

# Componente concreto
class MensagemBase(Mensagem):
    def enviar(self) -> str:
        return "Olá, essa é a mensagem base."

# Decorador abstrato
class DecoradorMensagem(Mensagem):
    def __init__(self, componente: Mensagem):
        self._componente = componente

    @abstractmethod
    def enviar(self) -> str:
        pass

# Decorador concreto: adiciona assinatura
class ComAssinatura(DecoradorMensagem):
    def enviar(self) -> str:
        return f"{self._componente.enviar()}\n\nAtenciosamente,\nPedro Henrique"

# Decorador concreto: adiciona rodapé
class ComRodape(DecoradorMensagem):
    def enviar(self) -> str:
        return f"{self._componente.enviar()}\n---\nMensagem enviada automaticamente."

# Decorador concreto: adiciona timestamp
class ComTimestamp(DecoradorMensagem):
    def enviar(self) -> str:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        return f"{self._componente.enviar()}\n\n[Enviado em: {agora}]"

# Uso
if __name__ == "__main__":
    mensagem = MensagemBase()
    
    # Empilhando decoradores
    mensagem_formatada = ComTimestamp(ComRodape(ComAssinatura(mensagem)))
    
    print(mensagem_formatada.enviar())
