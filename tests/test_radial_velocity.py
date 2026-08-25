import numpy as np
import pytest

from src.astro_simulations.radial_velocity import (
    calculate_radial_velocity,
    radial_velocity_curve,
    solve_kepler_equation,
)


def test_jupiter_around_the_sun():
    results = calculate_radial_velocity(1.0, 1.0, 5.2044, 90.0)

    assert results["semi_amplitude"] == pytest.approx(12.5, rel=0.02)
    assert results["period"] == pytest.approx(4332.0, rel=0.01)


def test_earth_around_the_sun():
    earth_in_jupiter_masses = 5.9722e24 / 1.898e27
    results = calculate_radial_velocity(1.0, earth_in_jupiter_masses, 1.0, 90.0)

    assert results["semi_amplitude"] == pytest.approx(0.089, rel=0.05)


def test_hot_jupiter_gives_a_large_signal():
    results = calculate_radial_velocity(1.11, 0.46, 0.0527, 90.0)

    assert results["semi_amplitude"] == pytest.approx(54.0, rel=0.05)
    assert results["period"] == pytest.approx(4.23, rel=0.05)


def test_period_matches_keplers_third_law():
    results = calculate_radial_velocity(1.0, 0.001, 1.0, 90.0)

    assert results["period"] == pytest.approx(365.25, rel=0.05)


def test_face_on_orbit_gives_no_signal():
    results = calculate_radial_velocity(1.0, 1.0, 1.0, 0.0)

    assert results["semi_amplitude"] == pytest.approx(0.0, abs=1e-12)
    assert results["minimum_mass"] == pytest.approx(0.0, abs=1e-12)


def test_minimum_mass_equals_true_mass_when_edge_on():
    assert calculate_radial_velocity(1.0, 2.5, 1.0, 90.0)["minimum_mass"] == pytest.approx(2.5)


def test_minimum_mass_underestimates_when_inclined():
    results = calculate_radial_velocity(1.0, 2.0, 1.0, 30.0)

    assert results["minimum_mass"] == pytest.approx(1.0, rel=1e-9)  # 2.0 * sin(30)


def test_mass_function_agrees_with_its_definition():
    results = calculate_radial_velocity(1.0, 1.0, 5.2044, 90.0)

    planet_kg, star_kg = 1.898e27, 1.989e30
    expected = planet_kg**3 / (star_kg + planet_kg) ** 2 / 1.989e30

    assert results["mass_function"] == pytest.approx(expected, rel=1e-6)


def test_kepler_equation_satisfies_the_identity():
    mean_anomaly = np.linspace(0.0, 2 * np.pi, 50)
    eccentric = solve_kepler_equation(mean_anomaly, 0.6)

    assert np.allclose(eccentric - 0.6 * np.sin(eccentric), mean_anomaly, atol=1e-9)


def test_kepler_equation_is_the_identity_for_a_circle():
    mean_anomaly = np.linspace(0.0, 2 * np.pi, 20)

    assert np.allclose(solve_kepler_equation(mean_anomaly, 0.0), mean_anomaly)


def test_circular_curve_is_a_symmetric_sinusoid():
    results = calculate_radial_velocity(1.0, 1.0, 1.0, 90.0)
    _, velocity = radial_velocity_curve(1.0, 1.0, 1.0, 90.0)

    assert velocity.max() == pytest.approx(results["semi_amplitude"], rel=1e-3)
    assert velocity.min() == pytest.approx(-results["semi_amplitude"], rel=1e-3)
    assert velocity.mean() == pytest.approx(0.0, abs=1e-3 * results["semi_amplitude"])


def test_curve_spans_exactly_one_period():
    results = calculate_radial_velocity(1.0, 1.0, 2.0, 90.0)
    time, _ = radial_velocity_curve(1.0, 1.0, 2.0, 90.0)

    assert time[0] == pytest.approx(0.0)
    assert time[-1] == pytest.approx(results["period"])


def test_eccentric_curve_is_asymmetric():
    results = calculate_radial_velocity(1.0, 1.0, 1.0, 90.0, eccentricity=0.5)
    k = results["semi_amplitude"]
    _, velocity = radial_velocity_curve(
        1.0, 1.0, 1.0, 90.0, eccentricity=0.5, argument_of_periastron=0.0
    )

    # v = K(cos(nu)+ e cos(omega)) with omega = 0 rides on a +0.5K offset
    assert velocity.max() == pytest.approx(1.5 * k, rel=0.02)
    assert velocity.min() == pytest.approx(-0.5 * k, rel=0.02)


def test_heavier_planet_gives_a_larger_signal():
    light = calculate_radial_velocity(1.0, 0.5, 1.0, 90.0)["semi_amplitude"]
    heavy = calculate_radial_velocity(1.0, 5.0, 1.0, 90.0)["semi_amplitude"]

    assert heavy > light


def test_wider_orbit_gives_a_smaller_signal():
    close = calculate_radial_velocity(1.0, 1.0, 0.1, 90.0)["semi_amplitude"]
    far = calculate_radial_velocity(1.0, 1.0, 5.0, 90.0)["semi_amplitude"]

    assert close > far
