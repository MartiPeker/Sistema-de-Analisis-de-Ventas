from abc import ABC, abstractmethod

class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, sales, products, customers, cities):
        pass