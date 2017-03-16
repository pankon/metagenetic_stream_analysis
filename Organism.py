#!/usr/bin/env python2

"""Organism: parent class for all organism types

    >>> Organism() # doctest: +ELLIPSIS
    Organism: [{'ratings': [], 'health': 100, 'factors': {'_mean': ..., '_min': ..., '_std': ..., '_max': ...}}, ...]
"""

from Factors import Factors

class Organism(object):
    def __init__(self, select_function = None, n_organisms = None, rating_function = None):
        n_organisms = n_organisms if n_organisms is not None else 2
        self.select_function = select_function if select_function is not None else lambda x: x
        self.rating_function = rating_function if rating_function is not None else lambda x: x
        self.instances = [self._gen_instance() for _ in range(n_organisms)]
        
    def __repr__(self):
        return "Organism: {}".format(str(self.instances))
        
    def _gen_instance(self):
        """Can be externalized if this becomes too complicated
        """
        return dict(
            factors = Factors.get_factors(),
            health = 100,
            ratings = []
        )
        
    def _rate_instances(self):
        for i_instance in range(len(self.instances)):
            self.instances[i_instance] = self.rating_function(self.instances[i_instance])
    
    def select(self):
        """Sort through all the grazers to determine the most fit.
        Call _breed() to create a number of organisms based on average
        fitness of this batch.
        """
        self._rate_instances()
        self.instances = self.select_function(self.instances)
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()   
