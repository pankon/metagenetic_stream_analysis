#!/usr/bin/env python2

"""Selector class - from a set of instances, return the best and make new ones

"""

class Selector(object):
    @classmethod
    def default_select(cls, instances):
        return instances
