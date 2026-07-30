import streamlit as st

LANGUAGES = {"English": "en", "Español": "es"}

TRANSLATIONS = {
    "en": {
        "app_title": "Welcome to the Astronomy Simulations",
        "sidebar_select": "Select a simulation above",
        "nav_home": "Home",
        "nav_kepler": "Kepler's Laws",
        "nav_planck": "Planck Spectrum",
        "landing_body": """
            This is an interactive collection of simulations designed to explore key concepts
            in astronomy. Each simulation allows you to adjust different physical parameters
            and see the results update in real time.

            ### Available Simulations
            - **Kepler's Laws** - Explore an elliptical orbit set by its semi-major axis and eccentricity,
            and see the Kepler's three laws: the ellipse shape, the perihelion-to-aphelion speed ratio,
            and the period-size relation $T^2 = a^3$.
            - **Planck Spectrum** - See how a blackbody's radiation depends on its temperature: the spectrum's peak
            shifts toward the blue as it heats up (Wien's law) and the total power grows as $T^4$
            (Stefan-Boltzmann law).

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
        # --- Kepler ---
        "kep_title": "Kepler's Laws Simulation",
        "kep_intro": """
        **Kepler's Laws** describe the motion of a body orbiting the Sun:

        - **1st law (ellipses):** the orbit is an ellipse with the Sun at one focus, its shape set by
        the semi-major axis $a$ and the eccentricity $e$ ($e = 0$ is a circle).
        - **2nd law (equal areas):** the body sweeps equal areas in equal times, so it moves fastest at
        perihelion and slowest at aphelion. The speed ratio is $v_\\mathrm{peri}/v_\\mathrm{aph} = (1+e)/(1-e)$.
        - **3rd law:** period and size are linked by $T^2 = a^3$ (with $a$ in AU and $T$ in years).

        Use the sidebar to set the semi-major axis and eccentricity, then click **Run Simulation** to see the
        orbit and its properties.
        """,
        "kep_semi_major": "Semi-major Axis (AU)",
        "kep_eccentricity": "Eccentricity",
        "kep_current_params": "Current parameters: a **{a} AU**, e **{e}**",
        "kep_orbit_title": "Orbit",
        "kep_x_axis": "x (AU)",
        "kep_y_axis": "y (AU)",
        "kep_hover": "x: %{x:.2f} AU<br>y: %{y:.2f} AU<extra></extra>",
        "kep_sun": "Sun",
        "kep_orbit": "Orbit",
        "kep_period": "Orbital Period",
        "kep_perihelion": "Perihelion",
        "kep_aphelion": "Aphelion",
        "kep_speed_ratio": "Speed Ratio (peri/aph)",
        # --- Planck ---
        "pl_title": "Planck Blackbody Spectrum Simulation",
        "pl_intro": """
        A **blackbody** absorbs all radiation and re-emits it with a spectrum that depends only on its temperature $T$.
        **Planck's law** gives the spectral radiance:

        $$B(\\lambda, T) = \\frac{2 h c^2}{\\lambda^5}\\,\\frac{1}{e^{hc/\\lambda k_B T} - 1}$$

        - **Wien's law:** the peak wavelength shifts inversely with temperature, $\\lambda_\\mathrm{peak} = b/T$.
        Hotter objects glow bluer.
        - **Stefan-Boltzmann law:** the total radiated power grows as $T^4$. Hotter objects are far brigther.

        Use the sidebar to set the temperature, then click **Run Simulation** to see the spectrum, its peak, and the
        total radiated power.
        """,
        "pl_temperature": "Temperature (K)",
        "pl_current_params": "Current parameters: T **{temp} K**",
        "pl_spectrum_title": "Blackbody Spectrum",
        "pl_wavelength_axis": "Wavelength (nm)",
        "pl_radiance_axis": "Spectral Radiance",
        "pl_hover": "Wavelength: %{x:.0f} nm<br>Radiance: %{y:.2e}<extra></extra>",
        "pl_visible": "Visible",
        "pl_peak_wavelength": "Peak Wavelength",
        "pl_radiated_power": "Radiated Power",
        "developed_by": "Developed by **Alexander Moreno Briceño** - Universidad Antonio Nariño",
    },
    "es": {
        "app_title": "Bienvenido a las Simulaciones de Astronomía",
        "sidebar_select": "Selecciona una simulación arriba",
        "nav_home": "Inicio",
        "nav_kepler": "Leyes de Kepler",
        "nav_planck": "Espectro de Planck",
        "landing_body": """
            Esta es una colección interactiva de simulaciones diseñada para explorar
            conceptos clave de astronomía. Cada simulación te permite ajustar diferentes parámetros
            físicos y ver los resultados actualizarse en tiempo real.

            ### Simulaciones disponibles
            - **Leyes de Kepler** - Explora una órbita elíptica definida por su semieje mayor y su excentricidad,
            y observa las tres leyes de Kepler: la forma de la elipse, la razón de rapidez perihelio-afelio y la
            relación periodo-tamaño $T^2 = a^3$.
            - **Espectro de Planck** - Observa cómo la radiación de un cuerpo negro depende de su temperatura: el máximo
            del espectro se desplaza hacia el azul al calentarse (ley de Wien) y la potencia total crece como
            $T^4$ (ley de Stefan-Boltzmann).

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
        # --- Kepler ---
        "kep_title": "Simulación de Leyes de Kepler",
        "kep_intro": """
        Las **Leyes de Kepler** describen el movimiento de un cuerpo que orbita el Sol:

        - **1ra ley (elipses):** la órbita es una elipse con el Sol en uno de sus focos, con su forma determinada
        por el semieje mayor $a$ y la excentricidad $e$ ($e = 0$ es un círculo).
        - **2da ley (áreas iguales):** el cuerpo barre áreas iguales en tiempos iguales, por lo que se mueve más rápido
        en el perihelio y más lento en el afelio. La razón de rapidez es $v_\\mathrm{peri}/v_\\mathrm{aph} = (1+e)/(1-e)$.
        - **3ra ley:** el periodo y el tamaño se relacionan por $T^2 = a^3$ (con $a$ en AU y $T$ en años).

        Use la barra lateral para definir el semieje mayor y la excentricidad, luego haz click en **Ejecutar Simulación**
        para ver la órbita y sus propiedades.
        """,
        "kep_semi_major": "Semieje Mayor (AU)",
        "kep_eccentricity": "Excentricidad",
        "kep_current_params": "Parámetros actuales: a **{a} AU**, e **{e}**",
        "kep_orbit_title": "Órbita",
        "kep_x_axis": "x (AU)",
        "kep_y_axis": "y (AU)",
        "kep_hover": "x: %{x:.2f} AU<br>y: %{y:.2f} AU<extra></extra>",
        "kep_sun": "Sol",
        "kep_orbit": "Órbita",
        "kep_period": "Periodo Orbital",
        "kep_perihelion": "Perihelio",
        "kep_aphelion": "Afelio",
        "kep_speed_ratio": "Razón de Rapidez (peri/afe)",
        # --- Planck ---
        "pl_title": "Simulación de la Radiación del Cuerpo Negro de Planck",
        "pl_intro": """
        Un **cuerpo negro** absorbe toda la radiación y la reemite con un espectro que depende únicamente de su
        temperatura $T$. La **ley de Planck** da la radiación espectral:

        $$B(\\lambda, T) = \\frac{2 h c^2}{\\lambda^5}\\,\\frac{1}{e^{hc/\\lambda k_B T} - 1}$$

        - **Ley de Wien:** la longitud de onda del máximo se desplaza de forma inversa a la temperatura, $\\lambda_\\mathrm{peak} = b/T$.
        Los objetos más calientes brillan en un tono azul.
        - **Ley de Stefan-Boltzmann:** la potencial total radiada crece como $T^4$. Los objetos más calientes son mucho más brillantes.

        Usa la barra lateral para definir la temperatura, luego haz click en **Ejecutar Simulación** para ver el
        espectro, su máximoo, y la potencia total radiada.
        """,
        "pl_temperature": "Temperatura (K)",
        "pl_current_params": "Parámetros actuales: T **{temp} K**",
        "pl_spectrum_title": "Radiación de Cuerpo Negro",
        "pl_wavelength_axis": "Longitud de Onda (nm)",
        "pl_radiance_axis": "Radiancia Espectral",
        "pl_hover": "Longitud de Onda: %{x:.0f} nm<br>Radiancia: %{y:.2e}<extra></extra>",
        "pl_visible": "Visible",
        "pl_peak_wavelength": "Longitud de Onda del Máximo",
        "pl_radiated_power": "Potencia Radiada",
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
    st.sidebar.page_link("pages/1_Kepler.py", label=t("nav_kepler"), icon="🪐")
    st.sidebar.page_link("pages/2_Planck_Spectrum.py", label=t("nav_planck"), icon="🌈")
