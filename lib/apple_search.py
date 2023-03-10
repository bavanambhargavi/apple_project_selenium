from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_search():
    # driver = webdriver.Chrome("./chromedriver")
    driver = webdriver.Chrome(service=Service(
         "D:\\Downloads\\chromedriver_win32\\chromedriver.exe"))
    # driver = webdriver.Chrome(
    # "D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    time.sleep(4)
    k = driver.find_element(By.XPATH, "//*[@id='5887ce50-a779-11ed-8691-0b0e22bacb60_label']/span")
    k.send_keys(Keys="EN")

