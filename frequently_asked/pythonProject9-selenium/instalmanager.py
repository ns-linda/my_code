from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import BY

driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.get("www.google.com")
driver.find_element(BY."Name")