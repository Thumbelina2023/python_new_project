import pytest

@pytest.mark.smoke
def test_decor_mark1(browser):
    assert True

@pytest.mark.regres
def test_decor_mark2(browser):
     assert True

@pytest.mark.regres
def test_decor_mark3(browser):
    assert True

@pytest.mark.regres
def test_decor_mark4(browser):
    assert True
