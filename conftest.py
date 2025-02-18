import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging
import os
import yaml

config_path = os.path.abspath("config/config.yaml")
print(f"Trying to open: {config_path}")

@pytest.fixture(scope="function")
def get_driver():
    """Setup and teardown of WebDriver."""
    # Load config file
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Set up WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(config["implicit_wait"])

    yield driver
    driver.quit()
