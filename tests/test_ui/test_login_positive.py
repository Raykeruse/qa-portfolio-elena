from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_page_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    assert username.is_displayed()
    assert password.is_displayed()
    assert login_button.is_displayed()
    assert login_button.get_attribute("value") == "Login"

    driver.quit()

