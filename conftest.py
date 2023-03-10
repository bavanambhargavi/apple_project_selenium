from selenium import webdriver
import pytest


@pytest.fixture
def main():
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://www.google.com/")
    driver.close()

    
