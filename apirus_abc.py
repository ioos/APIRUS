#!/usr/bin/env python

"""
The APIRUS API as an Abstract Base Class

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod


class APIRUS:
    """
    ABC for the API for Regular, Unstructured and Staggered model output
    (APIRUS)

    This ABC serves as a way to docuemnt the API, and is designed to be
    subclassed by py_ugrid, py_sgrid and any other future implementations.

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """
        this one is probably going to be very differenct for each subclass
        """
        pass

    @abstractmethod
    @classmethod
    def from_netcdf(cls, filename):
        """
        load a data set from a netcdf file
        """
        pass
