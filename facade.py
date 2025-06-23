# Facade
class HomeTheaterFacade:
    def __init__(self, projetor, dvd, som, luz):
        self.projetor = projetor
        self.dvd = dvd
        self.som = som
        self.luz = luz

    def assistir_filme(self, filme):
        print("\nIniciando o modo cinema")
        self.luz.apagar()
        self.projetor.ligar()
        self.som.ligar()
        self.dvd.ligar()
        self.dvd.play(filme)


# Subsistemas
class Projetor:
    def ligar(self):
        print("Porjetor ligado")

class DVDPplayer:
    def ligar(self):
        print("DVD ligado")

    def play(self, filme): 
        print(f"Reproduzindo {filme}")

class SistemaSom:
    def ligar(self):
        print("Som ligado")

class Luz:
    def apagar(self):
        print("Luzes apagadas")

# Cliente

if __name__ == "__main__":
    projetor = Projetor()
    dvd = DVDPplayer()
    som = SistemaSom()
    luz = Luz()
    
    home_theater = HomeTheaterFacade(projetor, dvd, som, luz)
    home_theater.assistir_filme("Matrix")