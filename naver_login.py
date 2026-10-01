import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def login_naver(username, password):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(2)
        driver.execute_script("document.getElementById('id').value = arguments[0];", username)
        time.sleep(1)
        driver.execute_script("document.getElementById('pw').value = arguments[0];", password)
        time.sleep(1)
        login_btn = driver.find_element(By.ID, "log.login")
        login_btn.click()
        time.sleep(10)
    finally:
        driver.quit()

if __name__ == "__main__":
    login_naver("YOUR_NAVER_ID", "YOUR_NAVER_PASSWORD")
