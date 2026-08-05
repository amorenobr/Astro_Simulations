import numpy as np
import pytest

from src.astro_simulations.transit import calculate_transit, transit_light_curve


def test_earth_transiting_the_sun():
    """Earth across the Sun: ~84 ppm deep, ~13 hours long."""
    r = calculate_transit(star_radius=1.0, planet_radius=1.0, semi_major_axis=1.0, period=365.25)
    assert r["radius_ratio"] == pytest.approx(1 / 109.076, rel=1e-3)
    assert r["depth_ppm"] == pytest.approx(84.0, rel=0.05)
    assert r["duration_total"] == pytest.approx(13.0, rel=0.05)


def test_jupiter_is_about_one_percent():
    """A Jupiter sized planet (11.2 R_earth) blocks ~1% of a Sun like star."""
    r = calculate_transit(1.0, 11.2, 1.0, 365.25)
    assert r["depth"] == pytest.approx(0.0105, rel=0.05)


def test_depth_scales_as_radius_ratio_squared():
    """Doubling the planet radius quadruples the depth."""
    small = calculate_transit(1.0, 5.0, 0.1, 30.0)
    large = calculate_transit(1.0, 10.0, 0.1, 30.0)
    assert large["depth"] == pytest.approx(4 * small["depth"])


def test_bigger_star_gives_shallower_transit():
    """The same planet is harder to detect around a larger star."""
    dwarf = calculate_transit(0.5, 2.0, 0.05, 10.0)
    giant = calculate_transit(2.0, 2.0, 0.05, 10.0)
    assert giant["depth"] < dwarf["depth"]


def test_full_duration_shorter_than_total():
    """T23 always fits inside T14."""
    r = calculate_transit(1.0, 11.2, 0.05, 3.0)
    assert 0 < r["duration_full"] < r["duration_total"]


def test_light_curve_shape():
    """Flux is 1 outside transit and dips to exactly 1 - depth at mid transit."""
    r = calculate_transit(1.0, 11.2, 0.05, 3.0)
    time, flux = transit_light_curve(1.0, 11.2, 0.05, 3.0, n=501)

    assert len(time) == len(flux) == 501
    assert flux[0] == pytest.approx(1.0)  # out of transit
    assert flux[-1] == pytest.approx(1.0)
    assert flux.min() == pytest.approx(1 - r["depth"])
    assert flux[np.argmin(np.abs(time))] == pytest.approx(1 - r["depth"])  # mid transit
    assert np.all(flux <= 1.0)
