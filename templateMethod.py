from abc import ABC, abstractmethod


# Classe Abstrata
class BebidaQuente(ABC):
    # metodo padrao
    def preparoBebida(self): 
        self.feverAgua()
        self.ingrediente()
        self.depejarXicara()
        self.adicionarComplemento()

    def feverAgua(self):
        print("Agua está sendo fervida")
    
    @abstractmethod
    def ingrediente(self):
        pass

    def depejarXicara(self):
        print("Depejando na xicara")
    
    @abstractmethod
    def adicionarComplemento(self):
        pass

# Classe Concreta
class Cafe(BebidaQuente):
    def ingrediente(self):
        print("Adicionando café")
    
    def adicionarComplemento(self):
        print("adicionando leite no café")

# Classe Concreta
class Cha(BebidaQuente):
    def ingrediente(self):
        print("Adicionando cha")
    
    def adicionarComplemento(self):
        print("Adicionando açucar no chá")



if __name__ == "__main__": 
    cafe = Cafe()
    cha = Cha()

    cafe.preparoBebida()
    print()
    cha.preparoBebida()


