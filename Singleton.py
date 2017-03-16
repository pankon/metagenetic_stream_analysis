#!/usr/bin/env python2

class Singleton(type):
    """From http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()