from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:\\Users\\Linda\\chromedriver.exe', options=options)

service  = Service("C:\\Users\\Linda\\chromedriver.exe")
# driver =  webdriver.Chrome(executable_path="C:\\Users\\Linda\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.get("https://google.com")
# pagetitle = driver.title
# assert "Google" in pagetitle , "Not found"

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)
username = driver.find_element(By.NAME,"NAME")
username.send_keys("Admin")
# driver.find