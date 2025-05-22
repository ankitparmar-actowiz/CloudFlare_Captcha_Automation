from seleniumbase import Driver
import time

driver = Driver(uc=True)
driver.maximize_window()

url = 'https://www.hisco.com'
driver.get(url)
time.sleep(5)

driver.uc_gui_click_captcha()
time.sleep(5)
