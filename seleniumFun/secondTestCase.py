from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select  

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:5500/htmlFun/index.html")
# driver.get("http://127.0.0.1:5500/htmlProject/contact.html") 

# Maximize browser
driver.maximize_window()

# Enter Data on the textbox
driver.find_element(By.NAME, "fullName").send_keys("Fritz Gayas")
driver.find_element(By.NAME, "emailAddress").send_keys("gayasfurittsu@gmail.com")
driver.find_element(By.NAME, "password").send_keys("2R3012JR")

# Handle dropdown (Favorite Coffee)
dropdown = Select(driver.find_element(By.NAME, "coffee"))

# You can select in different ways:
dropdown.select_by_visible_text("Iced Latte")   # select by visible text
# dropdown.select_by_index(10)                  # by index (0-based)