from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def test_gotowatch():
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys("apple")
    driver.find_element(
        By.XPATH, "//input[@title='Search']").send_keys(Keys.ENTER)
    driver.find_element(
        By.XPATH, "//span[normalize-space()='Apple - Official Site']").click()
    driver.find_element(
        By.XPATH, "//a[@aria-label='Watch']//span[@class='globalnav-link-text-container']").click()

    driver.quit()
