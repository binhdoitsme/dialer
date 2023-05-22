from dialer.domain.switch import Switch

import pytest


@pytest.fixture
def switch():
    s = Switch()
    s.add_pricing("operator A", "4673", 0.9)
    s.add_pricing("operator A", "46732", 1.1)
    s.add_pricing("operator B", "46", 1.0)
    s.add_pricing("operator B", "44", 0.8)
    return s


def test_routing(switch: Switch):
    assert switch.route("4473212345") == ("operator B", 0.8)
    assert switch.route("4673212345") == ("operator B", 1.0)
    assert switch.route("4673412345") == ("operator A", 0.9)
    assert switch.route("8473412345") == None


def test_add_pricing(switch: Switch):
    switch.add_pricing("operator A", "84", 0.12)
    assert switch._operators["operator A"].pricing_for("8473212345") == 0.12


if __name__ == "__main__":
    pytest.main()
