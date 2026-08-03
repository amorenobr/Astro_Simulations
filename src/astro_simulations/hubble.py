from typing import Dict

import numpy as np

c = 299792.458                # speed of light (km/s)
hubble_time_factor = 977.8    # Age [Gyr] = hubble_time_factor / H0 (H0 in km/s/Mpc)


def calculate_hubble(hubble_constant: float, distance: float) -> Dict[str, float]:
    """
    Hubble's Law: recession velocity, redshift, and the age of the Universe.

    Args:
        hubble_constant: The Hubble constant H0 in km/s/Mpc
        distance: The distance to the galaxy in megaparsecs (Mpc)

    Returns:
        A dictionary with the recession velocity (km/s), the redshift (low-z aprroximation
        z = v/c), and the age of the Universe (Hublle time in Gyr)
    """
    recession_velocity = hubble_constant * distance         # km/s
    redshift = recession_velocity / c                       # z ~ v/c (low redshift)
    age_of_universe = hubble_time_factor / hubble_constant  # Gyr (Hubble time = 1 H0)
    return {
            "recession_velocity": recession_velocity,
            "redshift": redshift,
            "age_of_universe": age_of_universe,
            }


def hubble_diagram(hubble_constant: float, max_distance: float = 500.0, n: int = 200):
    """
    The Hubble diagram: recession velocity vs. distance (the straight line v = H0 d).

    Returns:
        A tuple (distance, velocity) of NumPy arrays, in Mpc and km/s.
    """
    distance = np.linspace(0, max_distance, n)
    velocity = hubble_constant * distance
    return distance, velocity
