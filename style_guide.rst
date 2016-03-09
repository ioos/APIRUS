Style Guide for APIRUS related projects.
########################################

This document is designed to serve as a style guide for the APIRUS related pojects. The goal is to have a consistent coding style among the inter-related projects.

VERSION: 0.1

Overall Style
=============

Follow:

 - PEP 0008 -- Style Guide for Python Code

and

 - PEP 0257 -- Docstring Conventions

But there are more details that are unspecified in those documents, so those are clarified here.

Quote style
-----------

single vs double quotes? -- someone decide, I don't care :-)


Specifying parameters to functions in docstrings
------------------------------------------------

I think we should use either the "raw" sphinx approach::

  :param name: the value you want to pass in
  :type name: the type required for name

Or adopt the numpy extensions -- they are nicer, but require an extra plug-in...

https://pypi.python.org/pypi/numpydoc


Line Continuations
------------------

long lines need to get split, but there are multiple ways to do it.

Use un-closed brackets whenever possible to support continuation.

If a function definition or function call has too many parmaeters to all fit on one line, then put each on on it's own line. i.e.

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

Also, for literals for arrays of points that dont fit on one line (or maybe even if they do, alighing them logically is nice::


	the_points = [ (x1, y1),
	               (x2, y2),
	               (x3, y3),
	               (x4, y4),
	               (x5, y5),
	               (x6, y6),
	              ]

Also, putting the closing bracket on the next line and leaving a trailing comma, even after the last item, make it a lot easier to comment out and add in new items.


