# Estudo de caso: 1 (uma) chave e 3 (três) portas
# Para abrir as portas é disponibilizado apenas 1 (uma) chave, portanto utilize o padrão singleton para impedir a criação de mais chaves.

class Chave:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("passei aqui")
            cls._instancia = super().__new__(cls)
        return cls._instancia

class Porta():
    def __init__(self, nome):
        self.nome = nome
        self.aberta = False

    def abrirPorta(self, chave: Chave):
        if isinstance(chave, Chave):
            self.aberta = True
            print(f"Porta {self.nome}, aberta")
        else:
               print(f"Porta {self.nome}, não aberta")
    
if __name__ == "__main__":

    porta1 = Porta("A")
    porta2 = Porta("B")
    porta3 = Porta("C")

    chave_unica = Chave()

    porta1.abrirPorta(chave_unica)
    porta2.abrirPorta(chave_unica)
    porta3.abrirPorta(chave_unica)