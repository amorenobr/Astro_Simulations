from typing import Dict

import numpy as np

h = 6.62607015e-34          # Planck constant (J s)
c = 2.99792458e8            # speed of light (m/s)
k_B = 1.380649e-23          # Boltzmann constant (J/K)
b = 2.897771955e-3          # Wien's displacement constant (m K)
sigma = 5.670374419e-8      # Stefan-Boltzmann constant (W m^-2 K^-4)


def  calculate_planck(temperature: float) -> Dict[str, float]:
    """
    Blackbody radiations properties at a given temperature.

    Args:
        temperature: The blackbody temperature in Kelvin (K)

    Returns:
        A dictionary with the peak wavelength (Wien's law, in nm) and the total
        radiated power per unit area (Stefan-Boltzmann law in W/m^2)
    """
    peak_wavelength = b / temperature           # m
    radiated_power = sigma * temperature**4     # W/m^2
    return {
        "peak_wavelength": peak_wavelength * 1e9,   # convert to nm
        "radiated_power": radiated_power,
        }


def planck_spectrum(temperature: float, wavelength_min: float = 100.0, wavelength_max: float = 2500.0, n: int = 500):
    """
    Planck spectral radiance vs. wavelength for a blackbody at `temperature`.

    Wavelengths are in nanometers; the radiance is B(lambda, T) in SI units (W m^-2 sr^-1 m^-1).

    Returns:
        A tuple (wavelength_nm, radiance) of NumPy arrays.
    """
    wavelength_nm = np.linspace(wavelength_min, wavelength_max, n)
    lam = wavelength_nm * 1e-9
    radiance = (2 * h * c**2 / lam**5) / (np.exp(h * c / (lam * k_B * temperature)) - 1)
    return wavelength_nm, radiance
