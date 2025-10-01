# .\.venv\Scripts\activate
# pip install selenium
# pip install webdriver-manager

from selenium.webdriver import Chrome
from time import time
driver = Chrome()
driver.get("http://127.0.0.1:5500/htmlProject/contact.html")
