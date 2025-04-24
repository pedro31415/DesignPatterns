class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print('Passei aqui')
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
if __name__ == "__main__":
    instancia1 = Singleton()
    instancia2 = Singleton()

    print(instancia1)
    print(instancia1)
    print(instancia2)
    print(instancia1 == instancia2)
        
