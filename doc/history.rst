Setup, conventions and tools
============================



Conventions
-----------

1. Use Python version 3
1. Use the pandas, numpy,scipy and matplotlib
1. Documentation and tests will in Sphinx using the google
   documentation format rather numpydoc (which in turn is better than
   Sphinx .rst).

Setup
-----

#. Install Sphinx
#. Configure the documentation in the doc directory using
   ``spinx-quickstart`` to configure it. Select the following options:

   #) autodoc
   #) doctest
   #) document coverage
   #) pngmath
   #) viewcode 

#. Install ``numpydoc`` and add into the extensions list in
   ``conf.py''
#. Add a reference to the various ``intro.rst`` and ``history.rst``
   into ``index.rst``
#. Add ``numpydoc`` to the modules, e.g. ``tsi.py``.
