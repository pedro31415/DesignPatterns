from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperatura, umidade):
        pass

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperatura = None
        self._umidade = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperatura, self._umidade)

    def set_mudanca_clima(self, temperatura, umidade):
        print(f"\n[WeatherStation] Clima atualizado: {temperatura}°C, {umidade}% de umidade")
        self._temperatura = temperatura
        self._umidade = umidade
        self.notify_observers()

class Display(Observer):
    def update(self, temperatura, umidade):
        print(f"[Display] Temperatura: {temperatura}°C | Umidade: {umidade}%")

class Alert(Observer):
    def update(self, temperatura, umidade):
        if temperatura > 35:
            print("[Alert]  Alerta de onda de calor!")
        elif temperatura < 0:
            print("[Alert]  Alerta de congelamento!")

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

    # Mudança no estado
    weather_station.set_mudanca_clima(25, 60)
    weather_station.set_mudanca_clima(38, 40)
    weather_station.set_mudanca_clima(-5, 80)
