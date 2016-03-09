Style Guide for APIRUS related projects.
########################################

This document is designed to serve as a style guide for the APIRUS related projects.
The goal is to have a consistent coding style among the inter-related projects.

Overall Style
=============

Follow:

 - PEP 0008 -- Style Guide for Python Code

and

 - PEP 0257 -- Docstring Conventions

But there are more details that are unspecified in those documents, so those are clarified here.

Quote style
-----------

Triple double quotes for docstrings (see PEP257) and, when possible,
single quotes for strings.
 The reason for single quotes is to avoid making all python strings look like JSON.


Specifying parameters to functions in docstrings
------------------------------------------------

Write docstring in the numpydoc style.

https://pypi.python.org/pypi/numpydoc


Line Continuations
------------------

Long lines need to get split, but there are multiple ways to do it.

Use un-closed brackets whenever possible to support continuation.

If a function definition or function call has too many parameters to all fit on one line,
 then put each on on it's own line. i.e.

::

    def __init__(self,
                 node_lon=None,
                 node_lat=None,
                 center_lon=None,
                 center_lat=None,
                 edges=None,
                 node_padding=None,
                 edge1_padding=None,
                 edge2_padding=None,
                 grid_topology_var=None,
                 variables=None,
                 grid_variables=None,
                 dimensions=None,
                 node_dimensions=None,
                 node_coordinates=None,
                 edge1_coordinates=None,
                 edge2_coordinates=None,
                 angles=None,
                 )
not::

    def __init__(self, node_lon=None, node_lat=None, center_lon=None,
                 center_lat=None, edges=None, node_padding=None,
                 edge1_padding=None, edge2_padding=None, grid_topology_var=None,
                 variables=None, grid_variables=None, dimensions=None, node_dimensions=None, node_coordinates=None, edge1_coordinates=None,
                 edge2_coordinates=None, angles=None)

For literals arrays of points try to align them logically::


    the_points = [ (x1, y1),
                   (x2, y2),
                   (x3, y3),
                   (x4, y4),
                   (x5, y5),
                   (x6, y6),
                  ]

It is recommended to put the closing bracket on the next line and leave a trailing comma,
even after the last item, that makes it easier to comment out and add in new items.
