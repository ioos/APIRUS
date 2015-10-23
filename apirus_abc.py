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

    This ABC serves as a way to document the API, and is designed to be
    subclassed by py_ugrid, py_sgrid and any other future implementations.

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """
        this one is probably going to be very different for each subclass
        """
        pass

    @classmethod
    def load_grid(cls, grid):
        """
        load a data set from an arbitrary source

        :param grid: the grid you want to load. This could be:
                     * A string with a full path to a file, which could be any
                       supported file type -- probably netcdf
                     * a netcdf4 Dataset object
                     * a OpenDAP url
                     * possibley other supported APIs.

        :returns: returns an appropriate Grid object.

        This method will attempt to identify the type of the input grid, and
        call the appropriate loading methods.
        """
        pass


    @abstractmethod
    @classmethod
    def from_netcdf(cls, filename):
        """
        load a data set from a netcdf file
        """
        pass

    @abstractmethod
    def subset_rect(self, bounding_box):
        """
        subset the grid to the cells contained by the bounding box specified
        in lon-lat coordinates

        :param bounding_box: The bounding box, specified in lon-lat coords:
                             ( (min_lon, min_lat), (max_lon, max_lat))
        :type bounding_box: a 2x2 numpy array of float64, or any sequence that
                            can be turned into one.

        :returns: a new APIRUS object, of the same type as self.
        """
        pass

    @abstractmethod
    def subset_poly(self, polygon):
        """
        Subset the grid to the cells contained by an arbitrary polygon,
        specified in lon-lat coordinates

        :param polygon: The polygon, specified in lon-lat coords:
                             ( (lon1, lat1), (lon2, lat2), ..... )
        :type bounding_box: an Nx2 numpy array of float64, or any sequence that
                            can be turned into one.
        :returns: a new APIRUS object, of the same type as self.

        bounds are specified in lat-lon coords
        """
        pass

    @abstractmethod
    def to_ugrid(self):
        """
        return the same dataset, reformatted as a ugrid object. No
        interpolation or transformation is done.

        If self is already a ugrid object, it is returned unaltered

        If self can not be lovelessly converted, a TypeError is raised.
        """
        pass



