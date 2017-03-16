#!/usr/bin/env python2
"""Stock market implementation of CentralStation

    >>> a = CentralStation
    >>> a().prices
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> a().number_of_stocks
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
    >>> a().total_stock_costs
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]
"""

from CentralStation import CentralStation

class CentralStationStockMarket(CentralStation):

    def __init__(self):
        self.prices = [initial_stock_price for _ in range(n_logged)]
        self.number_of_stocks = [n_stocks_start for _ in range(n_logged)]
        self.total_stock_costs = [self.prices[i]*self.number_of_stocks[i] for i in range(n_logged)]
        
    def _increment(self, var_name):
        return dict(
        ) # TODO: Fill in with increment function
        
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
