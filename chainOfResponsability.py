from abc import ABC, abstractmethod

# Interface base
class SuporteHandler(ABC):
    def __init__(self):
        self._proximo = None
    
    def set_proximo(sellf, handler):
        sellf._proximo = handler
        return handler
    
    def tratar(self, problema):
        pass

# Handler Concreto
class Atendente(SuporteHandler):
    def tratar(self, problema):
        if problema == "senha esquecida":
            print("Atendente resolveu o problema: senha esquecida")
        elif self._proximo:
            print("Atendente não conseguiu resolver, encaminhando...")
            self._proximo.tratar(problema)

# Handler concreto
class Supervisor(SuporteHandler):
    def tratar(self, problema):
        if problema == "Erro no sistema":
            print("Supervisor resolveu o problema: Erro no sistema")
        elif self._proximo:
            print("Supervisor não consegui resolver, encaminhando")
            self._proximo.tratar(problema)

# Handler Concreto
class GerenteTecnico(SuporteHandler):
    def tratar(self, problema):
        if problema == "Falha no Servidor":
            print("Gerente écnicoresovleu o problema: Falha no Servidor")
        else: 
            print("Problema não resolvido. Abrir chamado avançado")
    
if __name__ == "__main__": 
    atendente = Atendente()
    supervisor = Supervisor()
    gerente = GerenteTecnico()

    atendente.set_proximo(supervisor).set_proximo(gerente)


    atendente.tratar("senha esquecida")
    print()
    atendente.tratar("Erro no sistema")
    print()
    atendente.tratar("Falha no Servidor")
    print()
    atendente.tratar("ERRO DESCONHECIDO")
    print()