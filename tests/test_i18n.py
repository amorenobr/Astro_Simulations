from src.astro_simulations.i18n import TRANSLATIONS, t


def test_translation_key_parity():
    """Every key must exist in both languages."""
    assert set(TRANSLATIONS["en"]) == set(TRANSLATIONS["es"])


def test_translate_falls_back_to_key():
    """t() returns the key itself when it's missing."""
    assert t("a_key_that_does_not_exist") == "a_key_that_does_not_exist"
