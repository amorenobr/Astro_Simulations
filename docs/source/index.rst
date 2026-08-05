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


Planck Spectrum
~~~~~~~~~~~~~~~

Models the radiation of a blackbody at temperature :math:`T`. The app plots the Planck spectral radiance versus
wavelength and reports the peak wavelength from Wien's law (:math:`\lambda_\mathrm{peak} = b/T`) and the total radiated
power per unit area from the Stefan-Boltzmann law (:math:`\sigma T^4`). The underlying calculations are implemented in
the :mod:`planck` module.


Hubble's Law
~~~~~~~~~~~~

Models the expansion of the Universe. Given the Hubble constant :math:`H_0` and a galaxy's distance :math:`d`,
the app plots the Hubble diagram (:math:`v = H_0 d`) and reports the recession velocity, the redshift
(:math:`z \approx v/c`), and the age of the Universe from the Hubble time (:math:`1/H_0`). The underlying
calculations are implemented in the :mod:`hubble` module.


Exoplanet Transit
~~~~~~~~~~~~~~~~~

Models the light curve of a planet transiting its star on a circular, edge-on orbit. Given the stellar and planetary
radii and the orbital distance, the app plots the trapezoidal light curve and reports the transit depth
:math:`(R_p/R_\star)^2`, the radius ratio, and the total and full durations :math:`T_{14}` and :math:`T_{23}`. The
orbital period follows from Kepler's third law. The underlying calculations are implemented in the :mod:`transit`
module.


API Reference
~~~~~~~~~~~~~

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
