from code import validate_info, win_ratio, positive_or_negative
import pytest

def main():
    test_validate()
    test_ratio()
    test_parity()

def test_validate():
     with pytest.raises(SystemExit):
        validate_info()

def test_ratio():
    assert win_ratio("9/6") == " Winning Record"
    assert win_ratio("6/9") == " Losing Record"
    assert win_ratio("3/3") == " Tying Record"

def test_parity():
    assert positive_or_negative(33) == " Super Positive"
    assert positive_or_negative(-33) == " Super Negative"
    assert positive_or_negative(0) == " Neutral"
