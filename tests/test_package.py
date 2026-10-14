import envseal


def test_version_is_exposed() -> None:
    assert envseal.__version__ == "0.0.1"


def test_public_surface_is_deliberately_small() -> None:
    # Guards the design rule: nothing becomes public by accident.
    assert set(envseal.__all__) == {"__version__"}
