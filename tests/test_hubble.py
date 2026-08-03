import pytest

from src.astro_simulations.hubble import calculate_hubble, hubble_diagram


def test_hubble_law_linear():
    """Recession velocity is H0 times distance."""
    r = calculate_hubble(hubble_constant=70.0, distance=100.0)
    assert r["recession_velocity"] == pytest.approx(7000.0)         # 70 * 100


def test_redshift_low_z():
    """Redshift is v/c in the low-redshift approximation."""
    r = calculate_hubble(70.0, 100.0)
    assert r["redshift"] == pytest.approx(7000.0 / 299792.458)


def test_age_of_universe():
    """Age = Hubble time = 1/H0 (H0 = 70 gives roughly 14 Gyr)."""
    r = calculate_hubble(70.0, 100.0)
    assert r["age_of_universe"] == pytest.approx(977.8 / 70.0)
    assert 13.5 < r["age_of_universe"] < 14.5


def test_higher_h0_means_younger_universe():
    """A larger Hubble constant implies a younger Universe."""
    young = calculate_hubble(100.0, 100.0)["age_of_universe"]
    old = calculate_hubble(50.0, 100.0)["age_of_universe"]
    assert young < old


def test_hubble_diagram():
    """A straight line through the origin with slope H0."""
    d, v = hubble_diagram(70.0, max_distance=500.0, n=100)
    assert len(d) == len(v) == 100
    assert d[0] == pytest.approx(0.0)
    assert v[0] == pytest.approx(0.0)
    assert v[-1] / d[-1] == pytest.approx(70.0)                      # slope = H0
