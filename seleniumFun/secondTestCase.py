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
driver.find_element(By.NAME, "fullName").clear()
driver.find_element(By.NAME, "fullName").send_keys("Fritz Adrian S. Gayas")

# Handle dropdown (Favorite Coffee)
dropdown = Select(driver.find_element(By.NAME, "coffee"))

# You can select in different ways:
dropdown.select_by_visible_text("Iced Latte")   # select by visible text
# dropdown.select_by_index(10)                  # by index (0-based)

# Working on Radio button
driver.find_element(By.XPATH, "//input[@id='chicken']").click()

# Working on Checkbox
driver.find_element(By.XPATH, "//input[@id='dog']").click()

# Working on Submit Button
# driver.find_element(By.XPATH, "//button[text()='Submit (GET)']").click() #Data is sent in the URL query string. For filtering and searching.
driver.find_element(By.XPATH, "//button[text()='Submit (POST)']").click() #Data is sent in the request body, not the URL.
