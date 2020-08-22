from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_options.add_argument(r"user-data-dir=C:\Users\lohfa\AppData\Local\Google\Chrome\User Data\Default Copy")

driver = webdriver.Chrome(options=chrome_options, executable_path=r'./chromedriver.exe')


driver.get('https://temptaking.ado.sg/group/aa254f4f1ea32e7664ce69c5eafb6530')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/select').click()
driver.find_element_by_xpath('//*[@id="member-select"]/option[32]').click()


driver.find_element_by_xpath('//*[@id="ep1"]').click()
pin = '8133'
i = 1
for num in pin:
    driver.find_element_by_xpath('//*[@id="ep'+str(i)+'"]').send_keys(int(num))
    i += 1

for i in range(5):
    randomTemp = random.randint(357,372)

i = 1
randomTemp = str(randomTemp)
for digit in randomTemp:
    driver.find_element_by_xpath('//*[@id="td'+str(i)+'"]').send_keys(int(digit))
    i += 1

driver.find_element_by_xpath('//*[@id="submit-temperature-container"]/button').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
driver.implicitly_wait(10)



driver.quit()
