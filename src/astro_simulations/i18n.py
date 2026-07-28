import streamlit as st

LANGUAGES = {"English": "en", "Español": "es"}

TRANSLATIONS = {
    "en": {
        "app_title": "Welcome to the Astronomy Simulations",
        "sidebar_select": "Select a simulation above",
        "nav_home": "Home",
        "landing_body": """
            This is an interactive collection of simulations designed to explore key concepts
            in astronomy. Each simulation allows you to adjust different physical parameters
            and see the results update in real time.

            ### Available Simulations

            ### How to Use
            1. Select a simulation from the **Sidebar** on the left
            2. Adjust the physical parameters using the sliders
            3. Click **Run Simulation** to generate the plot and view the results

            ### Documentation
            Full API and simulation documentation is available
            [here](https://amorenobr.github.io/Astro_Simulations/docs/).
            """,
        # --- Shared UI ---
        "sim_parameters": "Simulation Parameters",
        "run_simulation": "Run Simulation",
        "plots": "Plots",
        "sim_results": "Simulation Results",
        "sim_complete": "Simulation Complete!",
        "time_s": "Time (s)",
        "developed_by": "Developed by **Alexander Moreno Briceño** - Universidad Antonio Nariño",
    },
    "es": {
        "app_title": "Bienvenido a las Simulaciones de Astronomía",
        "sidebar_select": "Selecciona una simulación arriba",
        "nav_home": "Inicio",
        "landing_body": """
            Esta es una colección interactiva de simulaciones diseñada para explorar
            conceptos clave de astronomía. Cada simulación te permite ajustar diferentes parámetros
            físicos y ver los resultados actualizarse en tiempo real.

            ### Simulaciones disponibles

            ### Cómo usar la app
            1. Selecciona una simulación en la **barra lateral** de la izquierda
            2. Ajusta los parámetros físicos con los deslizadores
            3. Haz click en **Ejecutar simulación** para generar la gráfica y ver los resultados

            ### Documentación
            La documentación completa de la API y las simulaciones están
            disponibles [aquí](https://amorenobr.github.io/Astro_Simulations/docs/).
            """,
        # --- Shared UI ---
        "sim_parameters": "Parámetros de la Simulación",
        "run_simulation": "Ejecutar Simulación",
        "plots": "Gráficas",
        "sim_results": "Resultados de la Simulación",
        "sim_complete": "Simulación Completa!",
        "time_s": "Tiempo (s)",
        "developed_by": "Desarrollado por **Alexander Moreno Briceño** - Universidad Antonio Nariño",
    },
}


def get_lang() -> str:
    """Current language code (defaults to English)."""
    return st.session_state.get("lang", "en")


def t(key: str) -> str:
    """Translate a key for the current language; fall back to English, then the key."""
    lang = get_lang()
    return TRANSLATIONS.get(lang, {}).get(key) or TRANSLATIONS["en"].get(key, key)


def language_selector() -> None:
    """Render the sidebar: hide the default nav, add language toggle + translated nav."""
    st.markdown(
        """<style>
                [data-testid="stSidebarNav"] { display: none; }
                section[data-testid="stMain"],
                [data-testid="stAppViewContainer"] { scrollbar-gutter: stable; }
                </style>""",
        unsafe_allow_html=True,
    )
    choice = st.sidebar.radio(
        "🌐 Language / Idioma",
        list(LANGUAGES.keys()),
        horizontal=True,
        key="lang_selector",
    )
    st.session_state["lang"] = LANGUAGES[choice]

    # Translated page navigation (replaces the hidden, English-only default nav)
    st.sidebar.page_link("Simulations.py", label=t("nav_home"), icon="🏠")
