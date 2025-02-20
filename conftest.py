import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import yaml
import os

# Load the config files
config_path = os.path.abspath("config/config.yaml")
browserstack_config_path = os.path.abspath("config/browserstack.yaml")

with open(config_path, "r") as file:
    config = yaml.safe_load(file)

with open(browserstack_config_path, "r") as file:
    browserstack_config = yaml.safe_load(file)


@pytest.fixture(scope="function")
def get_driver():
    """Setup and teardown of WebDriver for either local or BrowserStack."""

    # Check if running on BrowserStack (environment variable or config setting)
    use_browserstack = os.getenv("USE_BROWSERSTACK", "false").lower() == "true"

    if use_browserstack:
        # Set up WebDriver for BrowserStack
        desired_caps = {
            "browser": browserstack_config["browserstack"]["capabilities"]["browser"],
            "browser_version": browserstack_config["browserstack"]["capabilities"]["browser_version"],
            "os": browserstack_config["browserstack"]["capabilities"]["os"],
            "os_version": browserstack_config["browserstack"]["capabilities"]["os_version"],
            "resolution": browserstack_config["browserstack"]["capabilities"]["resolution"],
            "name": browserstack_config["browserstack"]["capabilities"]["name"],
            "build": browserstack_config["browserstack"]["capabilities"]["build"]
        }

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # BrowserStack credentials
        username = browserstack_config["browserstack"]["username"]
        access_key = browserstack_config["browserstack"]["access_key"]

        # URL to connect to BrowserStack
        driver = webdriver.Remote(
            command_executor=f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_caps,
            options=options
        )
    else:
        # Set up WebDriver locally (e.g., Chrome)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.maximize_window()
    driver.implicitly_wait(config["implicit_wait"])

    yield driver
    driver.quit()
