from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.google.com')
driver.find_element(By.NAME, "q").send_keys("hugging face")
time.sleep(5)
suggestions = driver.find_elements(By.CSS_SELECTOR,"ul[role='listbox'] li")
for suggestion in suggestions[:5]:
    print(suggestion.text)




