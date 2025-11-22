class DataStore:
    def __init__(self):
        self.portfolios = dict()

    def get_portfolios(self):
        return [self.portfolios[b] for b in self.portfolios]

    def add_portfolio(self, portfolio):
        self.portfolios[portfolio.portfolio_id] = portfolio

    def update_portfolio(self, portfolio, update):
        for k in update:
            setattr(portfolio, k, update[k])

    def remove_portfolio(self, portfolio):
        del self.portfolios[portfolio.portfolio_id]
