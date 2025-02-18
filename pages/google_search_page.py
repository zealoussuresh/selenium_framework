from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.results = (By.CSS_SELECTOR, "h3")

    def load(self, url):
        """Load the Google homepage."""
        self.driver.get(url)

    def search(self, query):
        """Enter the search query and submit."""
        self.driver.find_element(*self.search_box).send_keys(query + Keys.RETURN)

    def get_results(self):
        """Retrieve search results."""
        return [element.text for element in self.driver.find_elements(*self.results)]
