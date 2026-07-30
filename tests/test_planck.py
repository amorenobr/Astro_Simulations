import numpy as np
import pytest

from src.astro_simulations.planck import calculate_planck, planck_spectrum


def test_wien_displacement_law():
    """Peak wavelength = b / T, and shifts inversely with temperature."""
    hot = calculate_planck(10000.0)
    cold = calculate_planck(5000.0)
    assert hot["peak_wavelength"] == pytest.approx(2.897771955e-3 / 10000.0 * 1e9, rel=1e-6)
    assert cold["peak_wavelength"] == pytest.approx(
        2 * hot["peak_wavelength"], rel=1e-6
    )  # half T -> 2x peak


def test_stefan_boltzmann_law():
    """Radiated power scales as T^4: doubling T gives 16x the power."""
    p1 = calculate_planck(5000.0)["radiated_power"]
    p2 = calculate_planck(10000.0)["radiated_power"]
    assert p2 / p1 == pytest.approx(2**4)


def test_spectrum_peak_matches_wien():
    """The spectrum's maximum sits at the Wien peak wavelength."""
    T = 6000.0
    wl, radiance = planck_spectrum(T, n=2000)
    peak_wl = wl[np.argmax(radiance)]
    assert peak_wl == pytest.approx(calculate_planck(T)["peak_wavelength"], rel=1e-2)
    assert len(wl) == len(radiance) == 2000


def test_spectrum_positive():
    """Radiance is positive across the range."""
    _, radiance = planck_spectrum(6000.0)
    assert np.all(radiance > 0)
