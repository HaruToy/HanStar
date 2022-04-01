import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

options=webdriver.ChromeOptions()
# 백그라운드 실행 옵션 추가
#options.add_argument("headless")
driver = webdriver.Chrome(chrome_options= options)

id='twitty3420'
pw='ghwlsvh4806'
GOAL='20'

driver.get('https://www.acmicpc.net/login?next=%2Fsso%3Fsso%3Dbm9uY2U9MmM3ZDIzZTFkNjRlMGQ0ZDU5Mzk2OGJkMjUyMzA3ZTU%253D%26sig%3Dfca1cf3149566c27f90312d9a6b395f49ba23aa5aedad0e3f79275e228f7253f%26redirect%3Dhttps%253A%252F%252Fsolved.ac%252Fapi%252Fv3%252Fauth%252Fsso%253Fprev%253D%25252Fevent%25252F220401')
driver.implicitly_wait(3)
#아이디 비번 입력
driver.find_element_by_name('login_user_id').send_keys(id)
driver.find_element_by_name('login_password').send_keys(pw)
#로그인
driver.find_element_by_id('submit_button').click()
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_xpath("//div[@class='col-md-6 col-sm-6']/a[@class='btn-u pull-right']").click()
time.sleep(3)
driver.implicitly_wait(3)
current_star=driver.find_element_by_xpath("//div[@style='text-align:center']/b[@style='font-size:1.5em']").text[:2]
while current_star<GOAL:
    driver.find_element_by_xpath("//button[@class='Button__ButtonContainer-sc-1ymjayw-0 eYKeLO']").click()
    time.sleep(1)

print(GOAL+"도착!!!!!")