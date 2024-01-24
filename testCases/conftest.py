import pytest
from selenium import webdriver

# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester Name"] = "Kunal"
    metadata.pop("Plugins", None)

@pytest.fixture(params=[
    ("TestUser101@credence.in", "Test123", "Pass"),
    ("TestUser101@credence.in1", "Test123", "Fail"),
    ("TestUser101@credence.in", "Test1231", "Fail"),
    ("TestUser101@credence.in1", "Test1231", "Fail")
])
def getDataForLogin(request):
    return request.param
