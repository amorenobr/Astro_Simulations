import plotly.graph_objects as go
import streamlit as st

from src.astro_simulations.i18n import language_selector, t
from src.astro_simulations.planck import calculate_planck, planck_spectrum

st.set_page_config(layout="wide")

language_selector()

st.title(t("pl_title"))
st.markdown(t("pl_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
temperature = st.sidebar.slider(t("pl_temperature"), 3000, 15000, 5800, step=100)

st.write(t("pl_current_params").format(temp=temperature))

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    results = calculate_planck(temperature)

    # Plotting
    st.subheader(t("plots"))

    wavelength, radiance = planck_spectrum(temperature)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wavelength, y=radiance, mode="lines", hovertemplate=t("pl_hover")))
    # Shade the visible band (380-750 nm) and mark the Wien peak
    fig.add_vrect(
        x0=380,
        x1=750,
        fillcolor="orange",
        opacity=0.12,
        line_width=0,
        annotation_text=t("pl_visible"),
        annotation_position="top",
    )
    fig.add_vline(x=results["peak_wavelength"], line_dash="dash", line_color="gray")
    fig.update_layout(
        title=t("pl_spectrum_title"),
        xaxis_title=t("pl_wavelength_axis"),
        yaxis_title=t("pl_radiance_axis"),
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
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor="gray",
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2 = st.columns(2)
    col1.metric(t("pl_peak_wavelength"), f"{results['peak_wavelength']:.0f} nm")
    col2.metric(t("pl_radiated_power"), f"{results['radiated_power']:.2e} W/m^2")
