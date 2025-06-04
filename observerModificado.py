from abc import ABC, abstractmethod

class EventNotifier:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class Subject(ABC):
    def __init__(self):
        self.observer = EventNotifier()
    
    def attach(self, observer):
        self.observer.attach(observer)
    
    def detach(self, observer):
        self.observer.detach(observer)
    
    def notify(self, data):
        self.observer.notify(data)
    
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temperatura = None
        self.umidade = None

    def set_mudanca_clima(self, temperatura, umidade):
        print(f"\n[WeatherStation] Clima atualizado: {temperatura}°C, {umidade}% de umidade")
        self.temperatura = temperatura
        self.umidade = umidade
        self.notify({'temperatura': temperatura, 'umidade': umidade})

class Display(Observer):
    def update(self, data):
        print(f"[Display] Temperatura: {data['temperatura']}ºC | umidade: {data['umidade']}%")

class Alert(Observer):
    def update(self, data):
        temperatura = data['temperatura']
        if temperatura > 35:
            print("[ALERT] -> Tá ficando quente")
        elif temperatura < 0:
            print("[ALERT] -> Congelamento")

class Logger(Observer):
    def update(self, data):
        print(f"[Logger] Dados registrados: {data['temperatura']}°C, {data['umidade']}%")

if __name__ == "__main__":
    weather_station = WeatherStation()

    display = Display()
    alert = Alert()
    logger = Logger()

    weather_station.attach(display)
    weather_station.attach(alert)
    weather_station.attach(logger)

    weather_station.set_mudanca_clima(25, 60)
    weather_station.set_mudanca_clima(-3, 20)
    weather_station.set_mudanca_clima(46, 40)