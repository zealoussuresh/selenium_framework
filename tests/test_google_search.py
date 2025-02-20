import pytest

from pages.google_search_page import GoogleSearchPage



def test_google_search(get_driver):
    """Verify Google search functionality."""
    driver = get_driver
    google = GoogleSearchPage(driver)

    google.load("https://www.google.com")
    google.search("Python Selenium")

    results = google.get_results()
    assert any("Selenium" in result for result in results), "No relevant results found."


def test_google_search_second_query(get_driver):
    """Verify another Google search test."""
    driver = get_driver
    google = GoogleSearchPage(driver)

    google.load("https://www.google.com")
    google.search("OpenAI ChatGPT")

    results = google.get_results()
    assert any("ChatGPT" in result for result in results), "No relevant results found."
