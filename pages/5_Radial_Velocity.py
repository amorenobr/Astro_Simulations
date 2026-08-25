import plotly.graph_objects as go
import streamlit as st

from src.astro_simulations.i18n import language_selector, t
from src.astro_simulations.radial_velocity import calculate_radial_velocity, radial_velocity_curve

st.set_page_config(layout="wide")

language_selector()

st.title(t("rv_title"))
st.markdown(t("rv_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
stellar_mass = st.sidebar.slider(t("rv_stellar_mass"), 0.1, 3.0, 1.0, step=0.05)
planet_mass = st.sidebar.slider(t("rv_planet_mass"), 0.01, 15.0, 1.0, step=0.01)
semi_major_axis = st.sidebar.slider(t("rv_semi_major"), 0.01, 10.0, 1.0, step=0.01)
inclination = st.sidebar.slider(t("rv_inclination"), 0.0, 90.0, 90.0, step=1.0)
eccentricity = st.sidebar.slider(t("rv_eccentricity"), 0.0, 0.8, 0.0, step=0.05)
argument_of_periastron = st.sidebar.slider(t("rv_periastron"), 0.0, 360.0, 90.0, step=5.0)

results = calculate_radial_velocity(
    stellar_mass, planet_mass, semi_major_axis, inclination, eccentricity
)

st.write(
    t("rv_current_params").format(
        ms=stellar_mass, mp=planet_mass, a=semi_major_axis, p=f"{results['period']:.2f}"
    )
)

# Main Simulation
if st.button(t("run_simulation")):
    time, velocity = radial_velocity_curve(
        stellar_mass,
        planet_mass,
        semi_major_axis,
        inclination,
        eccentricity,
        argument_of_periastron,
    )
    semi_amplitude = results["semi_amplitude"]

    # Plotting
    st.subheader(t("plots"))

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=time,
            y=velocity,
            mode="lines",
            name=t("rv_star_Velocity"),
            hovertemplate=t("rv_hover"),
        )
    )
    fig.add_hline(y=0.0, line_width=1, line_color="gray")
    fig.add_hline(y=semi_amplitude, line_width=1, line_dash="dash", line_color="lightgray")
    fig.add_hline(y=-semi_amplitude, line_width=1, line_dash="dash", line_color="gray")

    fig.update_layout(
        title=t("rv_curve_title"),
        xaxis_title=t("rv_time_axis"),
        yaxis_title=t("rv_velocity_axis"),
        plot_bgcolor="white",
    )
    fig.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=False,
    )
    fig.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor="gray",
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("rv_period"), f"{results['period']:.2f} d")
    col2.metric(t("rv_semi_amplitude"), f"{semi_amplitude:.2f} m/s")
    col3.metric(
        t("rv_minimum_mass"),
        f"{results['minimum_mass']:.3f} MJ",
        delta=t("rv_true_mass").format(m=f"{planet_mass:.3f}"),
        delta_color="off",
    )
    col4.metric(t("rv_mass_function"), f"{results['mass_function']:.3e} M⊙")
