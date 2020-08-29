from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import time

url = 'https://temptaking.ado.sg/group/88d917959c0fa1fc5a9ed61b9052ab7c'

def run():

    driver = webdriver.Chrome()
    driver.get(url)

    driver_wait = WebDriverWait(driver, 25)
    driver_wait.until(element_to_be_clickable((By.ID, "member-select"))).click()

    driver.find_element_by_xpath("//*[@id='member-select']/option[text()='Ryan Loh']").click()

    driver.find_element_by_id('ep1').click()
    pin = '8133'
    for i, num in enumerate(pin):
        driver.find_element_by_id('ep'+str(i + 1)).send_keys(int(num))

    randomTemp = str(random.randint(357,372))
    for i, digit in enumerate(randomTemp):
        driver.find_element_by_id('td'+str(i + 1)).send_keys(int(digit))

    driver.find_element(By.CLASS_NAME, 'btn btn-warning').click()

    submit_wait = WebDriverWait(driver, 30)
    submit_wait.until(element_to_be_clickable((By.ID, 'submit-temp-btn'))).click()

    driver.quit()

if __name__ == '__main__':
    run()
