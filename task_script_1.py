import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")


# search = driver.find_element(By.NAME,"q")
# search.send_keys("dhaka")


try:
    search = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME,"q"))
    )

    search.send_keys("dhaka")

    time.sleep(5)
    search.send_keys(Keys.RETURN)


except:
    driver.quit()


