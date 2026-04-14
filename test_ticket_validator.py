import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_validate_ticket_true():
    newCode = "TK999999"
    result = validate_ticket(newCode)
    assert result == True

def test_validate_ticket_len():
    newcode = "TK99999"
    result = validate_ticket(newcode)
    assert result == False

def test_validate_ticket_prefix():
    newCode = "SH999999"
    result = validate_ticket(newCode)
    assert result == False

def test_validate_ticket_str():
    newcode = 99999999
    with pytest.raises(TypeError):
        validate_ticket(newcode)

def test_get_tier_invalid():
    newCode = "SH999999"
    with pytest.raises(ValueError):
        get_ticket_tier(newcode)

def test_get_tier_VIP():
    newcode = "TK699999"
    result = get_ticket_tier(newcode)
    assert result == "VIP"

def calculate_total_empty_price():
    newprices = []
    with pytest.raises(ValueError):
        get_ticket_tier(newprices)

def calculate_total_dicount_out_range():
    newprices = [25.0, 50.0, 75.0, 100.0]
    newdiscount = 100
    with pytest.raises(ValueError):
        get_ticket_tier(newprices, newdiscount)

def calculate_total_price_not_lst():
    newprices = "25.0, 50.0, 75.0 100.0"
    with pytest.raises(TypeError):
        get_ticket_tier(newprices)

def calculate_total_price_correct():
    newprices = [25.0, 50.0, 75.0, 100.0]
    result = calculate_total(newprices)
    assert result == 250.0

