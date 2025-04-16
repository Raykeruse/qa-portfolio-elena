from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_with_empty_username():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error.is_displayed()
    assert "Epic sadface: Username is required" in error.text

    driver.quit()


def test_login_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("wrong_password")
    driver.find_element(By.ID,"login-button").click()

    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error.is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in error.text

    driver.quit()
