# def test_hdl_analysis_normal():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(65)
#     expected = "Normal"
#     assert answer == expected

# def test_hdl_analysis_bl():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(45)
#     expected = "Borderline Low"
#     assert answer == expected

# def test_hdl_analysis_low():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(15)
#     expected = "Low"
#     assert answer == expected

# def test_hdl_analysis(): # not the preferred method
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(65)
#     expected = "Normal"
#     assert answer == expected
#     answer = hdl_analysis(45)
#     expected = "Borderline Low"
#     assert answer == expected
#     answer = hdl_analysis(15)
#     expected = "Low"
#     assert answer == expected


import pytest


@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (15, "Low")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected

# @pytest.mark.parametrize("in_string,expected",[
#     ("ab",True),
#     ("abc",False),
#     ("123456",False)])
# def test_check_input(in_string,expected):
#     from blood_calculator import check_input
#     answer = check_input(in_string)
#     assert answer == expected
