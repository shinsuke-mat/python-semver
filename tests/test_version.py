from python_semver.version import Version
import pytest


@pytest.mark.parametrize("verstr", [
    "1.2.3",
    "1.2.99",
    "1.99.3",
    "0.0.0",
    "10.20.30",
    "99999.99999.99999",
])
def test_version_valid(verstr):
    v = Version(verstr)
    reconstructed = f"{v.major}.{v.minor}.{v.patch}"
    assert reconstructed == verstr

@pytest.mark.parametrize("verstr", [
    "1",
    "1.2",
    "1.2.",
    "1..3",
    "a1.2.3a",
    "aaa",
    "1.01.1",
    "1. 2.3",
    "1.-2.3",
])
def test_version_invalid(verstr):
    with pytest.raises(ValueError):
        Version(verstr)
