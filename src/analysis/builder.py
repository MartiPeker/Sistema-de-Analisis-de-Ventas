class ReportBuilder:
    def __init__(self):
        self._strategies = []
        self._context = None

    def with_strategy(self, strategy):
        self._strategies.append(strategy)
        return self

    def build(self):
        from .context import AnalysisContext
        self._context = AnalysisContext(self._strategies[0]) if self._strategies else None
        return self

    def execute_all(self, sales, products, customers, cities):
        results = {}
        for strategy in self._strategies:
            self._context.set_strategy(strategy)
            name = strategy.__class__.__name__.replace("Strategy", "")
            results[name] = self._context.execute_analysis(sales, products, customers, cities)
        return results