from abc import ABC, abstractmethod

class ConexaoBanco(ABC):
    def efetuarConsulta(self):
        self.conectar()
        self.executarConsulta()
        self.desconectar()

    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def executarConsulta():
        pass

    @abstractmethod
    def desconectar():
        pass


class Oracle(ConexaoBanco):
    def conectar(self):
        print("Conectando...")
    
    def executarConsulta(self):
        print("Executando consulta...")
    
    def desconectar(self):
        print("Serviço desconectado")


class SQLServer(ConexaoBanco):
    def conectar(self):
        print("Conectando...")

    def executarConsulta(self):
        print("Executando consulta...")
    
    def desconectar(self):
        print("Serviço desconectado")


if __name__ == "__main__":
    oracle  = Oracle()
    oracle.efetuarConsulta()

    sqlServer = SQLServer()
    sqlServer.efetuarConsulta()