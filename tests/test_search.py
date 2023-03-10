from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_search():
    # driver = webdriver.Chrome("./chromedriver")
    # driver = webdriver.Chrome(service=Service(
    #  "D:\\Downloads\\chromedriver_win32\\chromedriver.exe"))
    driver = webdriver.Chrome(executable_path=
        "D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    driver.save_screenshot("..\\data\\apple1.png")
    driver.quit()
