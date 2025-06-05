import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, dados):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self, dados):
        for observer in self._observers:
            observer.update(dados)

class ConcreteSubject(Subject):
    def __init__(self, filepath):
        super().__init__()
        self.df = pd.read_csv(filepath)

    def filtrar_por_especie(self, especie):
        dados_filtrados = self.df[self.df['species'] == especie]
        self.notify(dados_filtrados)

class PizzaObserver(Observer):
    def update(self, dados):
        count = dados['species'].value_counts()
        count.plot.pie(autopct='%1.1f%%', figsize=(5,5))
        plt.title("Distribuição das Espécies")
        plt.ylabel('')
        plt.show()

class HistogramaOberserver(Observer):
    def update(self, dados):
        plt.figure(figsize=(7,5))
        sns.histplot(dados['sepal_length'], kde=True)
        plt.title("Histograma -  Tamaho da Sépala")
        plt.xlabel("Comprimento da Sépala")
        plt.show()

class TabelaObserver(Observer):
    def update(self, dados):
        print("Exibindo os primeiros registros filtrados:")
        print(dados.head())


if __name__ == "__main__":

    base_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

    dataset = ConcreteSubject(base_url)

    pizza = PizzaObserver()
    histograma = HistogramaOberserver()
    tabela = TabelaObserver()

    dataset.attach(pizza)
    dataset.attach(histograma)
    dataset.attach(tabela)

    dataset.filtrar_por_especie("setosa")