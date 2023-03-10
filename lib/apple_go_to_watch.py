from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_gotoiphone():
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Apple - Official Site']").click()
    time.sleep(4)
    driver.find_element(
        By.XPATH, "//a[@aria-label='Watch']//span[@class='globalnav-link-text-container']").click()
    time.sleep(4)

    driver.quit()
