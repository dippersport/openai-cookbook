from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

def login(username, password):
    options = Options()
    options.add_argument("--disable-infobars")

    # Убедитесь, что путь к драйверу Chrome указан в системной переменной PATH
    # Или передайте полный путь к драйверу без executable_path
    driver_path = 'chromedriver'  # Имя драйвера (должен быть в PATH)

    browser = webdriver.Chrome(options=options)

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()



login("ceyhun071173@mail.ru", "Kingsport123.")
#browser = webdriver.Chrome('../chromedriver/chromedriver')