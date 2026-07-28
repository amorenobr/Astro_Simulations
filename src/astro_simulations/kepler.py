from typing import Dict

import numpy as np


def calculate_kepler(semi_major_axis: float, eccentricity: float) -> Dict[str, float]:
    """
    Calculates orbital properties from Kepler's laws for a body orbiting the Sun.

    Uses solar units: the semi-major axis in astronomical units (AU) gives the period
    in years via Kepler's third law (T^2 = a^3).

    Args:
        semi_major_axis: The semi-major axis of the orbit in AU
        eccentricity: The orbital eccentricity (0 = circle, closer to 1 = elongated)

    Returns:
        A dictionary with the semi-minor axis, perihelion and aphelion distances,
        orbital period, and the perihelion to aphelion speed ratio.

    """

    semi_minor_axis = semi_major_axis * np.sqrt(1 - eccentricity**2)
    perihelion = semi_major_axis * (1 - eccentricity)
    aphelion = semi_major_axis * (1 + eccentricity)
    period = semi_major_axis**1.5  # in years (Kepler's third law)
    speed_ratio = (1 + eccentricity) / (1 - eccentricity)  # v_peri / v_aph (Kepler's second law)

    return {
        "semi_minor_axis": semi_minor_axis,
        "perihelion": perihelion,
        "aphelion": aphelion,
        "period": period,
        "speed_ratio": speed_ratio,
    }


def orbit_shape(semi_major_axis: float, eccentricity: float, n: int = 500):
    """
    Points tracing the elliptical orbit with the Sun at one focus (origin), using the focus
    centered polar form r = a(1 - e^2) / (1 + e cos(theta)).

    Returns:
        A tuple (x, y) of Numpy arrays, in AU.
    """

    theta = np.linspace(0, 2 * np.pi, n)
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y
