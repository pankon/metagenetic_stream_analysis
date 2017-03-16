#!/usr/bin/env python2

"""The grazer class is a simple genetic algorithm upon which the higher-level organisms derive their strategies from in various degrees of separation. 

Grazers deal directly with real-world data.

    >>> grazers = Grazers()
    >>> grazers.select()
    >>> grazers.instances # doctest: +ELLIPSIS
    [{'ratings': [], 'health': 100, 'factors': {...}, ...]
    >>> grazers.cs.container # doctest: +ELLIPSIS
    [...]
    >>> grazers # doctest: +ELLIPSIS
    Grazers: [{'ratings': [], 'health': 100, 'factors': {'_mean': ..., '_min': ..., '_std': ..., '_max': ...}}, ...]
    >>> grazers.select()
    
"""

from CentralStation import CentralStation, n_grazers
from Organism import Organism
import numpy as np

class Grazers(Organism):
    
    cs = CentralStation()
    
    def __init__(self, select_function = None, rating_function = None, n_organisms = None):
        n_organisms = n_organisms if n_organisms is not None else n_grazers
        super(Grazers, self).__init__(select_function = select_function, rating_function = rating_function, n_organisms = n_organisms)
        
    def __repr__(self):
        return "Grazers: {}".format(str(self.instances))
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()   
    
