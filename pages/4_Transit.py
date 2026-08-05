import plotly.graph_objects as go
import streamlit as st

from src.astro_simulations.i18n import language_selector, t
from src.astro_simulations.transit import calculate_transit, transit_light_curve

st.set_page_config(layout="wide")

language_selector()

st.title(t("tr_title"))
st.markdown(t("tr_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
star_radius = st.sidebar.slider(t("tr_star_radius"), 0.2, 2.0, 1.0, step=0.05)
planet_radius = st.sidebar.slider(t("tr_planet_radius"), 1.0, 15.0, 11.2, step=0.1)
semi_major_axis = st.sidebar.slider(t("tr_semi_major"), 0.01, 1.0, 0.05, step=0.01)

# Orbital period from Kepler's third law for a Sun-like star (T^2 = a^3)
period = semi_major_axis**1.5 * 365.25

st.write(
    t("tr_current_params").format(
        rs=star_radius, rp=planet_radius, a=semi_major_axis, p=f"{period:.1f}"
    )
)

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    results = calculate_transit(star_radius, planet_radius, semi_major_axis, period)

    # Plotting
    st.subheader(t("plots"))

    time, flux = transit_light_curve(star_radius, planet_radius, semi_major_axis, period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=flux, mode="lines", hovertemplate=t("tr_hover")))
    # Shade the transit window and mark the out of transit baseline
    fig.add_vrect(
        x0=-results["duration_total"] / 2,
        x1=results["duration_total"] / 2,
        fillcolor="steelblue",
        opacity=0.10,
        line_width=0,
        annotation_text=t("tr_transit"),
        annotation_position="top",
    )
    fig.add_hline(y=1.0, line_dash="dash", line_color="gray")
    fig.update_layout(
        title=t("tr_curve_title"),
        xaxis_title=t("tr_time_axis"),
        yaxis_title=t("tr_flux_axis"),
        plot_bgcolor="white",
        showlegend=False,
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
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(t("tr_depth"), f"{results['depth_ppm']:.0f} ppm")
    col2.metric(t("tr_radius_ratio"), f"{results['radius_ratio']:.4f}")
    col3.metric(t("tr_duration_total"), f"{results['duration_total']:.2f} h")
    col4.metric(t("tr_duration_full"), f"{results['duration_full']:.2f} h")
