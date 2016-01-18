Setup, conventions and tools
============================



Conventions
-----------

#. Use Python version 3
#. Use the pandas, numpy,scipy and matplotlib
#. Documentation and tests will in Sphinx using the google
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
#. Install ``napoleon`` extension and enable it
#. Add a reference to the various ``intro.rst`` and ``history.rst``
   into ``index.rst``
#. Add google doc to the modules, e.g. ``exdoc.py``.
#. See ```exdoc.py'' for examples following the google conventions.
