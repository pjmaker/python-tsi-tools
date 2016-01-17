Setup, conventions and tools
============================



Conventions
-----------

1. Use Python version 3
1. Use the pandas, numpy,scipy and matplotlib
1. Documentation and tests will in Sphinx using the numpydoc
   extension.

Setup
-----

1. Install Sphinx
1. Configure the documentation in the doc directory using
   ``spinx-quickstart`` to configure it. Select the following options:
   a. autodoc
   a. doctest
   a. document coverage
   a. pngmath
   a. viewcode 
1. Install ``numpydoc`` and add into the extensions list in
   ``conf.py''
1. Add a reference to the various ``intro.rst`` and ``history.rst``
   into ``index.rst``
1. Add ``numpydoc`` to the modules, e.g. ``tsi.py``.
