import testdata.constants as dataVal
import pytest
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                    help="Type in Your Browser Name e.g chrome,Firefox")

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='ie':
        driver=webdriver.Ie()

    driver = webdriver.Chrome()
    driver.get(dataVal.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()
