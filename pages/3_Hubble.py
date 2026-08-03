import plotly.graph_objects as go
import streamlit as st

from src.astro_simulations.hubble import calculate_hubble, hubble_diagram
from src.astro_simulations.i18n import language_selector, t

st.set_page_config(layout="wide")

language_selector()

st.title(t("hub_title"))
st.markdown(t("hub_intro"))

# Sidebar for inputs
st.sidebar.header(t("sim_parameters"))
hubble_constant = st.sidebar.slider(t("hub_h0"), 50, 100, 70)
distance = st.sidebar.slider(t("hub_distance"), 0, 500, 100)

st.write(t("hub_current_params").format(h0=hubble_constant, d=distance))

# Main Simulation
if st.button(t("run_simulation")):
    # Calculations
    results = calculate_hubble(hubble_constant, distance)

    # Plotting
    st.subheader(t("plots"))

    d_line, v_line = hubble_diagram(hubble_constant, max_distance=500.0)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=d_line, y=v_line, mode="lines", name=t("hub_line"), hovertemplate=t("hub_hover")
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[distance],
            y=[results["recession_velocity"]],
            mode="markers",
            name=t("hub_galaxy"),
            marker={"size": 12, "color": "crimson"},
            hovertemplate=t("hub_hover"),
        )
    )
    fig.update_layout(
        title=t("hub_diagram_title"),
        xaxis_title=t("hub_distance_axis"),
        yaxis_title=t("hub_velocity_axis"),
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
    )
    st.plotly_chart(fig, width="stretch")

    # Results
    st.subheader(t("sim_results"))
    st.success(t("sim_complete"))

    col1, col2, col3 = st.columns(3)
    col1.metric(t("hub_velocity"), f"{results['recession_velocity']:.0f} km/s")
    col2.metric(t("hub_redshift"), f"{results['redshift']:.4f}")
    col3.metric(t("hub_age"), f"{results['age_of_universe']:.2f} Gyr")
