from typing import Dict

import numpy as np

earth_radii_per_solar_radius = 109.076  # R_sun / R_earth
solar_radius_in_au = 0.00465047  # R_sun in AU


def calculate_transit(
    star_radius: float, planet_radius: float, semi_major_axis: float, period: float
) -> Dict[str, float]:
    """
    Transit geometry for a planet crossing its star, assuming a circular, edge-on orbit
    (central transit, impact parameter b=0).

    Args:
        star_radius: Stellar radius in solar radii (R_sun)
        planet_radius: Planet radius in Earth radii (R_earth)
        semi_major_axis: Orbital semi-major axis in AU
        period: Orbital period in days

    Returns:
        A dictionary with the transit depth (fraction and parts per million), the planet-to-star radius
        ratio, the total duration T14 (first to fourth contact in hours), and the full duration T23 (flat
        bottom in hours).
    """
    radius_ratio = (planet_radius / earth_radii_per_solar_radius) / star_radius
    depth = radius_ratio**2  # (R_planet / R_star)^2

    star_radius_au = star_radius * solar_radius_in_au
    planet_radius_au = (planet_radius / earth_radii_per_solar_radius) * solar_radius_in_au
    period_hours = period * 24.0

    # T14: first to fourth contact. T23: second to third contact
    duration_total = (period_hours / np.pi) * np.arcsin(
        (star_radius_au + planet_radius_au) / semi_major_axis
    )
    duration_full = (period_hours / np.pi) * np.arcsin(
        (star_radius_au - planet_radius_au) / semi_major_axis
    )

    return {
        "depth": depth,
        "depth_ppm": depth * 1e6,
        "radius_ratio": radius_ratio,
        "duration_total": duration_total,
        "duration_full": duration_full,
    }


def transit_light_curve(
    star_radius: float, planet_radius: float, semi_major_axis: float, period: float, n: int = 500
):
    """
    Trapezoidal transit light curve: constant flux out of transit, linear ingress and egress ramps,
    and a flat bottom of depth (R_planet / R_star)^2 during T23.

    Time is centered on mid-transit and spans three times the total duration T14.

    Returns:
        A tuple (time_hours, relative_flux) of NumPy arrays.
    """
    results = calculate_transit(star_radius, planet_radius, semi_major_axis, period)
    depth = results["depth"]
    half_total = results["duration_total"] / 2
    half_full = results["duration_full"] / 2

    time = np.linspace(-1.5 * results["duration_total"], 1.5 * results["duration_total"], n)
    abs_time = np.abs(time)

    flux = np.ones(n)
    flux = np.where(abs_time <= half_full, 1 - depth, flux)
    ramp = (half_total - abs_time) / (half_total - half_full)  # 1 at T23, 0 at T14
    on_ramp = (abs_time > half_full) & (abs_time <= half_total)
    flux = np.where(on_ramp, 1 - depth * ramp, flux)

    return time, flux
