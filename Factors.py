#!/usr/bin/env python2

"""Factors for the current experiment

    >>> Factors.get_factors() # doctest: +ELLIPSIS
    {'_mean': ..., '_min': ..., '_std': ..., '_max': ...}
    
    >>> Factors.get_factor_list()
    ['_std', '_max', '_min', '_mean']
    
    >>> Factors.load_factor_analysis([[0,3,4], [1,2,4], [1, 2, 100]])
    [{'_mean': 2.3333333333333335, '_min': 0, '_std': -2.220446049250313e-16, '_max': 4}, {'_mean': 2.3333333333333335, '_min': 1, '_std': -2.220446049250313e-16, '_max': 4}, {'_mean': 34.333333333333336, '_min': 1, '_std': -7.105427357601002e-15, '_max': 100}]

      
    >>> Factors.individual_factor_analysis({'_std': 0.25, '_max': 0.25, '_min': 0.25, '_mean': 0.25})
    [1.5833333333333333, 1.8333333333333333, 33.83333333333333]
    
"""

from CentralStation import random_float

class Factors(object):

    @classmethod
    def get_factor_list(cls):
        return ['_std', '_max', '_min', '_mean']
    
    @classmethod
    def get_factors(cls):
        return dict([key, random_float()] for key in cls.get_factor_list())
        
    @classmethod
    def load_factor_analysis(cls, container):
        cls.analysis_list = []
        for option_list in container:
            factor_dict = {}
            cls.mean_called_bool = False
            cls.sum_called_bool = False
            for factor_name in cls.get_factor_list():            
                # note/ TODO: this is inefficient and soo slow, but allows easy
                # extension of factors. It would be good to store this info once
                # instead of going over it each time for a cs.container set.
                factor_dict[factor_name] = getattr(cls, factor_name)(option_list)
            cls.analysis_list.append(factor_dict)
        return cls.analysis_list

    @classmethod
    def individual_factor_analysis(cls, dict_factors):
        factor_list = cls.get_factor_list()
        return [sum(dict_factors[key] * factor_dict[key] for key in factor_dict.keys()) for factor_dict in cls.analysis_list] # assume all containers are the same
            
    @classmethod
    def _mean(cls, option_list):
        if not cls.mean_called_bool:
            cls.mean_called_bool = True
            cls.__mean = cls._sum(option_list)/float(len(option_list))
        return cls.__mean
            
    @classmethod
    def _sum(cls, option_list):
        if not cls.sum_called_bool:
            cls.sum_called_bool = True
            cls.__sum = sum(option_list)
        return cls.__sum
        
    @classmethod
    def _max(cls, option_list):
        return max(option_list)
        
    @classmethod
    def _min(cls, option_list):
        return min(option_list)
    
    @classmethod    
    def _std(cls, option_list):
        return sum([item - cls._mean(option_list) for item in option_list])/float(len(option_list)-1)
       
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
