from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_filter_products_by_category():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/products")

    try:
        buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Consent')]")
        for btn in buttons:
            if btn.is_displayed() and btn.is_enabled():
                driver.execute_script("arguments[0].click();", btn)
                break
    except Exception as e:
        print(f"Couldn't click consent button: {e}")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#Women']"))
    ).click()

    driver.find_element(By.CSS_SELECTOR, "#Women > div > ul > li:nth-child(1) > a").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo"))
    )

    products = driver.find_elements(By.CLASS_NAME, "productinfo")
    assert len(products) > 0, "No products found!"

    for product in products:
        text = product.text.lower()
        print(text)
        assert "dress" in text

    driver.quit()