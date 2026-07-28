import streamlit as st

from src.astro_simulations.i18n import language_selector, t

st.set_page_config(
    page_title="Astronomy Simulations",
    layout="wide",
)

language_selector()

st.title(t("app_title"))
st.markdown(t("landing_body"))
st.sidebar.success(t("sidebar_select"))

st.divider()
st.caption(t("developed_by"))
