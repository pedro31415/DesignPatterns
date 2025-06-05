from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.observers = []

    
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade):
        pass

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temperatura = None
        self.umidade = None

    def add_observer(self, observer):
        self.observers.append(observer)
        print(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperatura, self.umidade)
    
    def set_mudanca_clima(self, temperatura, umidade):
        print(f"\n[WeatherStation] Clima atualizado: {temperatura}°C, {umidade}% de umidade")
        self.temperatura = temperatura
        self.umidade = umidade
        self.notify_observers()

class Display(Observer):
    def update(self, temperatura, umidade):
        print(f"[Display] Temperatura: {temperatura}ºC | umidade: {umidade}%")

class Alert(Observer):
    def update(self, temperatura, umidade):
        if temperatura > 35:
            print("[ALERT] -> Tá ficando quente")
        elif temperatura < 0:
            print("[ALERT] -> Congelamento")

class Logger(Observer):
    def update(self, temperatura, umidade):
        print(f"[Logger] Dados registrados: {temperatura}°C, {umidade}%")


if __name__ == "__main__":
    weather_station = WeatherStation()

    display = Display()
    alert = Alert()
    logger = Logger()

    weather_station.add_observer(display)
    weather_station.add_observer(alert)
    weather_station.add_observer(logger)

    weather_station.set_mudanca_clima(25, 60)
    weather_station.set_mudanca_clima(-3, 20)
    weather_station.set_mudanca_clima(46, 40)




