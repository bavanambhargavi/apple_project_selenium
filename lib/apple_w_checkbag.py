from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_gotowatch():
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Apple - Official Site']").click()
    driver.find_element(
        By.XPATH, "//a[@aria-label='Watch']//span[@class='globalnav-link-text-container']").click()
    driver.find_element(
        By.CSS_SELECTOR, "li[class='chapternav-item chapternav-item-series-8'] span[class='chapternav-label']").click()
    driver.find_element(By.CLASS_NAME, "ac-ln-button").send_keys(Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, "button[id='name-0-0'] span").click()
    driver.find_element(By.CSS_SELECTOR, ".colornav-swatch").click()
    driver.find_element(By.CLASS_NAME, "form-selector-label").click()
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Make calls and send messages with just your Apple Watch.']").click()
    time.sleep(1)
    driver.find_element(By.NAME, "add-to-cart").click()
    driver.find_element(
        By.CLASS_NAME, "button button-block button-super").click()

    driver.quit()
