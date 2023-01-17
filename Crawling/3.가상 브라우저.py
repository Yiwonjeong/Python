"""
날짜: 2023/01/17
이름: 이원정
내용: 파이썬 가상 브라우저 크롤링 실습하기

sudo python3 -m pip install selenium
sudo python3 -m pip install webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 가상 브라우저 실행 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver', options=chrome_options)

# 네이버 이동
browser.get('http://naver.com')

# 로그인 클릭
btnLogin = browser.find_element(By.CSS_SELECTOR, '#account > a')    # find_element: 선택자 함수
btnLogin.click()

# 아이디, 비밀번호 입력
input_id = browser.find_element(By.CSS_SELECTOR, '#id')
input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')
input_id.send_keys('abcd')
input_pw.send_keys('1234')

# 최종 로그인 버튼 클릭
btnSubmit= browser.find_element(By.CSS_SELECTOR, '#log\.login')
btnSubmit.click()
