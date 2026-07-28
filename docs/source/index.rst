.. Astro_Simulations documentation master file, created by
   sphinx-quickstart on Thu Feb 19 11:51:53 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Astronomy Simulations Documentation
===================================

This is the documentation for all the astronomy simulations. Each simulation is an interactive Streamlit app that lets you 
modify physical parameters and see the results update in real time.

Simulations
-----------

Kepler's Laws
~~~~~~~~~~~~~

Models a body orbiting the Sun in solar units. Given the semi-major axis :math:`a` (in AU) and eccentricity :math:`e`,
the app draws the elliptical orbit with the Sun at one focus and reports the perihelion and aphelion distancess, the
orbital period from Kepler's third law :math:`T^2 = a^3`, and the perihelion-to-aphelion speed ratio
:math:`(1+e)/(1-e)`. The underlying calculations are implemented in the :mod:`kepler` module.


API Reference
~~~~~~~~~~~~~

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
