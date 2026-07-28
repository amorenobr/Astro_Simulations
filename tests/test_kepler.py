import numpy as np
import pytest

from src.astro_simulations.kepler import calculate_kepler, orbit_shape


def test_circular_orbit():
    """Zero eccentricity is a circle: minor = major, peri = aph, uniform speed."""
    r = calculate_kepler(semi_major_axis=1.0, eccentricity=0.0)
    assert r["semi_minor_axis"] == pytest.approx(1.0)
    assert r["perihelion"] == pytest.approx(1.0)
    assert r["aphelion"] == pytest.approx(1.0)
    assert r["period"] == pytest.approx(1.0)        # Earth: a = 1 AU, T = 1 year
    assert r["speed_ratio"] == pytest.approx(1.0)   # uniform speed on a circle


def test_kepler_third_law():
    """T^2 = a^3 in solar units."""
    a = 4.0
    r = calculate_kepler(a, 0.2)
    assert r["period"] ** 2 == pytest.approx(a**3)  # 8^2 == 64 == 4^3


def test_eccentric_orbit():
    """Nonzero eccentricity: peri < a < aph, and faster at perihelion."""
    a, e = 2.0, 0.5
    r = calculate_kepler(a, e)
    assert r["perihelion"] == pytest.approx(1.0)    # a(1 - e)
    assert r["aphelion"] == pytest.approx(3.0)      # a(1 + e)
    assert r["perihelion"] < a < r["aphelion"]
    assert r["speed_ratio"] == pytest.approx(3.0)   # (1 + e)/(1 - e)


def test_orbit_shape_on_ellipse():
    """Traced points span perihelion to aphelion from the focus."""
    a, e = 2.0, 0.4
    x, y = orbit_shape(a, e, n=360)
    r = np.sqrt(x**2 + y**2)
    assert len(x) == len(y) == 360
    assert r.min() == pytest.approx(a * (1 - e), rel=1e-2)  # perihelion
    assert r.max() == pytest.approx(a * (1 + e), rel=1e-2)  # aphelion
