from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time


def test_openlink():
    # driver = webdriver.Chrome(service=Service(
    # "D:\\Downloads\\chromedriver_win32\\chromedriver.exe"))
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Apple - Official Site']").click()
    # driver.find_element(By.ID, "ac-ls-continue").click()
    driver.save_screenshot("..\\data\\apple2.png")
    time.sleep(4)
    driver.quit()
