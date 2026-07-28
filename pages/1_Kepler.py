import plotly.graph_objects as go
import streamlit as st

from src.astro_simulations.i18n import language_selector, t
from src.astro_simulations.kepler import calculate_kepler, orbit_shape

st.set_page_config(layout="wide")

language_selector()

st.title(t("kep_title"))
st.markdown(t("kep_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
semi_major_axis = st.sidebar.slider(t("kep_semi_major"), 0.5, 30.0, 1.0)
eccentricity = st.sidebar.slider(t("kep_eccentricity"), 0.0, 0.9, 0.2)

st.write(t("kep_current_params").format(a=semi_major_axis, e=eccentricity))

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    results = calculate_kepler(semi_major_axis, eccentricity)

    # Plotting
    st.subheader(t("plots"))

    x, y = orbit_shape(semi_major_axis, eccentricity)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=x, y=y, mode="lines", name=t("kep_orbit"), hovertemplate=t("kep_hover"))
    )
    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers",
            name=t("kep_sun"),
            marker={"size": 14, "color": "gold"},
            hoverinfo="name",
        )
    )
    fig.update_layout(
        title=t("kep_orbit_title"),
        xaxis_title=t("kep_x_axis"),
        yaxis_title=t("kep_y_axis"),
        plot_bgcolor="white",
    )
    fig.update_xaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor="gray",
    )
    fig.update_yaxes(
        ticks="outside",
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor="gray",
        scaleanchor="x",
        scaleratio=1,
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("kep_period"), f"{results['period']:.2f} yr")
    col2.metric(t("kep_perihelion"), f"{results['perihelion']:.2f} AU")
    col3.metric(t("kep_aphelion"), f"{results['aphelion']:.2f} AU")
    col4.metric(t("kep_speed_ratio"), f"{results['speed_ratio']:.2f}")
