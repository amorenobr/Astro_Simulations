from typing import Dict

import numpy as np

gravitational_constant = 6.674e-11  # m^3 kg^⁻1 s^-2
solar_mass = 1.989e30  # kg
jupiter_mass = 1.898e27  # kg
astronomical_unit = 1.495978707e11  # m
seconds_per_day = 86400.0  # s


def calculate_radial_velocity(
    stellar_mass: float,
    planet_mass: float,
    semi_major_axis: float,
    inclination: float,
    eccentricity: float = 0.0,
) -> Dict[str, float]:
    """
    Reflex motion of star pulled by an orbiting planet, as seen along the line of sight.

    Star and planet orbit their common center of mass. Only the component of the star's velocity along the line
    is measurable as a Doppler shift, so an orbit seen face on produces no signal at all.

    Args:
        stellar_mass: Mass of the star in solar masses
        planet_mass: True mass of the planet in Jupiter masses
        semi_major_axis: Semi-major axis of the planet's orbit in AU
        inclination: Orbital inclination in degrees (90 is edge on, 0 is face on)
        eccentricity: Orbital eccentricity, 0 for a circular orbit

    Returns:
        A dictionary with the orbital period in days, the velocity semi-amplitude K in m/s, the minimum mass
        M sin i in Jupiter masses, the mass function in solar masses, and the radius of the star's own orbit
        about the barycenter in AU,
    """
    star_kg = stellar_mass * solar_mass
    planet_kg = planet_mass * jupiter_mass
    total_kg = star_kg + planet_kg
    axis_m = semi_major_axis * astronomical_unit

    sin_i = np.sin(np.deg2rad(inclination))

    period_s = 2 * np.pi * np.sqrt(axis_m**3 / (gravitational_constant * total_kg))

    # K = (M_p sin i / sqrt(1 - e^2)) * sqrt(G / (M_total * a))
    semi_amplitude = (
        planet_kg
        * sin_i
        / np.sqrt(1 - eccentricity**2)
        * np.sqrt(gravitational_constant / (total_kg * axis_m))
    )

    # What an observer recovers from the curve alone
    mass_function = (
        period_s
        * semi_amplitude**3
        * (1 - eccentricity**2) ** 1.5
        / (2 * np.pi * gravitational_constant)
    )

    return {
        "period": period_s / seconds_per_day,
        "semi_amplitude": semi_amplitude,
        "minimum_mass": planet_mass * sin_i,
        "mass_function": mass_function / solar_mass,
        "star_orbit_radius": axis_m * planet_kg / total_kg / astronomical_unit,
    }


def solve_kepler_equation(
    mean_anomaly: np.ndarray,
    eccentricity: float,
    tolerance: float = 1e-10,
    max_iterations: int = 50,
) -> np.ndarray:
    """
    Solves Kepler's equation M = E - e sin(E) for the eccentricity anomaly E.

    The equation is trascendental, so it is solved by Newton-Raphson iteration. Starting from E = M + e sin(M) it
    converges for the eccentricities of real planetary orbits.

    Args:
        mean_anomaly: Mean anomaly M in radians, which advances uniformly with time
        eccentricity: Orbital eccentricity, 0 <= e < 1
        tolerance: Stop once the largest residual M - (E - e sin E) falls below this in absolute value
        max_iterations: Stop after this many steps

    Returns:
        A NumPy array of eccentric anomalies in radians, the same shape as mean_anomaly.
    """
    eccentric_anomaly = mean_anomaly + eccentricity * np.sin(mean_anomaly)

    for _ in range(max_iterations):
        residual = eccentric_anomaly - eccentricity * np.sin(eccentric_anomaly) - mean_anomaly
        if np.all(np.abs(residual) < tolerance):
            break
        eccentric_anomaly = eccentric_anomaly - residual / (
            1 - eccentricity * np.cos(eccentric_anomaly)
        )

    return eccentric_anomaly


def radial_velocity_curve(
    stellar_mass: float,
    planet_mass: float,
    semi_major_axis: float,
    inclination: float,
    eccentricity: float = 0.0,
    argument_of_periastron: float = 90.0,
    n: int = 500,
):
    """
    Line-of-sight velocity of the star over one full orbit.

    A circular orbit gives a pure sinusoid. Eccentricity distorts it, and the argument of periastron sets how the
    distortion is oriented towards us, so the same eccentricity can produce a sharp spike or a broad trough depending
    on the viewing geometry.

    Args:
        stellar_mass: Mass of the star in solar masses
        planet_mass: True mass of the planet in Jupiter masses
        semi_major_axis: Semi-major axis of the planet's orbit in AU
        inclination: Orbital inclination in degrees
        eccentricity: Orbital eccentricity, 0 for a circular orbit
        argument_of_periastron: Angle from the ascending node to periastron in degrees
        n: Number of samples over the orbit

    Returns:
        A tuple (time, velocity) of NumPy arrays, in days and m/s.
    """
    results = calculate_radial_velocity(
        stellar_mass, planet_mass, semi_major_axis, inclination, eccentricity
    )
    period = results["period"]
    semi_amplitude = results["semi_amplitude"]

    time = np.linspace(0.0, period, n)
    mean_anomaly = 2 * np.pi * time / period
    eccentric_anomaly = solve_kepler_equation(mean_anomaly, eccentricity)

    true_anomaly = 2 * np.arctan2(
        np.sqrt(1 + eccentricity) * np.sin(eccentric_anomaly / 2),
        np.sqrt(1 - eccentricity) * np.cos(eccentric_anomaly / 2),
    )

    omega = np.deg2rad(argument_of_periastron)
    velocity = semi_amplitude * (np.cos(true_anomaly + omega) + eccentricity * np.cos(omega))

    return time, velocity
