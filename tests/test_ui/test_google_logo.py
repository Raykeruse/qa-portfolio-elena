from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_logo_is_displayed():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    logo = driver.find_element(By.XPATH,  "//img[@alt='Google']")

    assert logo.is_displayed()
    driver.quit()
