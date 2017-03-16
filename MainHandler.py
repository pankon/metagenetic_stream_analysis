#!/usr/bin/env python2

"""Main file for running learning experiment

"""

from CentralStation import CentralStation
from Grazers import Grazers
import logging

_n_default_cycles = 100

class MainHandler(object):
    """Main handler for this experiment
    """

    cs = CentralStation()
    grazers = Grazers()
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    
    def __init__(self):
        pass
        
    def run(self, n_cycles = None):
        n_cycles = n_cycles if n_cycles else _n_default_cycles
        for i_cycle in xrange(n_cycles):
            self.cs.increment_time()
            self._select()
            self.logger.info(self.cs.container)
            self.logger.info(self._winners)
        return self._winners       
    
    # Generating fluctuations of market is handled externally
    
    def _select(self):
        self.grazers.select()
    
    @property    
    def _winners(self):
        return dict(
            grazers = self.grazers.instances
        )
        
if __name__ == '__main__':
    mh = MainHandler()
    cs = CentralStation()
    mh.run(5)
