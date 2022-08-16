from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(driver.title)

# search = driver.find_element_by_name("s")
# search.clear()
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

try:
    accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ytd-button-renderer[2]//a[1]//tp-yt-paper-button[1]//yt-formatted-string[1]"))
    )
    accept.click()

    time.sleep(0.500)
    

    fullscreen = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//button[@title='Schermo intero (f)']"))
    )
    fullscreen.click()
    

except:
    driver.quit()
