from ix_liquid.mass_balance import estimate_train


def test_mass_balance_basic():
    result = estimate_train(8.0, 0.3, 0.5)
    assert round(result.recovered_or_removed_gpm, 3) == 5.2
    assert round(result.effluent_gpm, 3) == 2.8


def test_invalid_separator_fraction():
    try:
        estimate_train(8.0, 1.2, 0.5)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
