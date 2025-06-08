class AnalysisContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_analysis(self, sales, products, customers, cities):
        return self._strategy.analyze(sales, products, customers, cities)