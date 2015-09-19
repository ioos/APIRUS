***************
APIRS Use Cases
***************

This document will server to capture the use cases we want the API to cover.

The actual API to do this will get documented elsewhere.

The CF/CDM GRID object (we have been calling this "RGRID") is really just a specific type of SGRID object, so perhaps we only need to write code to deal with SGRID and UGRID?

We need tools that will work with a dataset object that can have SGRID or UGRID objects as children. We need to have ways of instantiating these objects, and methods that work with them.

Instantiation
=============

    ability to create these objects from local netcdf files or remote opendap datasets (and eventually other services like CDMremote).
    check for compliance with SGRID or UGRID and if valid, return the appropriate object.
    allow the user to fix or supply missing information so that valid SGRID or UGRID objects can be created
    not load any coordinate data or data values


Core Uses
==========

The core uses are about data extraction

* subsetting by bounding box in real coordinates (x,y) or (lon,lat)
* vertical slices (transects) along arbitrary (x,y) paths, and also (x,y,t) paths
* trajectories along arbitrary (x,y), (x,y,z) and (x,y,z,t) paths
* horizontal transects at specific z level, depth below surface, and height above bottom
* velocity vectors rotated to north/east and averaged or interolated to user-specified locations (e.g. node, face, edge)
* extract timeseries profile using different interpolations schemes (nearest, linear) to a specified lon,lat location
* extract timeseries using different interpolations schemes (nearest, linear in x,y space, spline in depth) to specified (lon,lat,z location)


Higher Level Analysis
=====================

This is analysis stuff -- beyond jsut accessing the data.

* isosurfaces
* total amount over specified region
* vorticity
