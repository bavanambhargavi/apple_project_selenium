from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_openlink():
    driver = webdriver.Chrome(
        "D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
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
    driver.find_element(By.ID, "ac-ls-continue").click()
    time.sleep(4)
    driver.quite()
