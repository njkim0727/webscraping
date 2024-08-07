from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://daum.net"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_id("q").clear()
browser.find_element_by_id("q").send_keys("헬리오시티")
browser.find_element_by_xpath(
    "//*[@id='daumSearch']/fieldset/div/div/button[2]").click()
browser.find_element_by_xpath(
    "//*[@id='estateColl']/div[2]/div/div[2]/div[1]/a").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='__next']/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div/div/div[1]")))
    # 성공했을 때 동작 수행
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()


time.sleep(10)
source = browser.page_source
soup = BeautifulSoup(source, "lxml")
print(soup.prettify())
