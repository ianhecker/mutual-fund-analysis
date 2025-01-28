import pytest
from src.calculations import calculate_future_value

@pytest.mark.parametrize(
    "principal, gross_annual_return, compounds_per_year, years, expected",
    [
        (0, 0, 0, 0, 0),
        (100, 0.01, 1, 1, 101.0),
        (10000, 0.082, 4, 5,  15005.84),
        (100000, 1.0, 4, 30, 4.25795984000815e+16),
    ],
)
def test_calculate_future_value(principal, gross_annual_return, compounds_per_year, years, expected):
    result = calculate_future_value(principal, gross_annual_return, compounds_per_year, years)
    assert round(result, 2) == expected
