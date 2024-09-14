import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    act = ActionChains(driver)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.act = act
    yield
    driver.close()
