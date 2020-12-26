from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = (r"C:\Users\christopher\Desktop\chromedriver.exe")
driver = webdriver.Chrome(path)

driver.get("https://play.typeracer.com")
driver.maximize_window()

link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@title="Keyboard shortcut: Ctrl+Alt+I"]'))).click()
stuff = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@unselectable= 'on']")))
words = []
for i in stuff:
    words.append(i.text)
if len(words) == 3:
    words[0:2] = [''.join(words[0:2])]
words = ' '.join(words)
words = words.split()
race = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
hello = input("press any key to start typing")
for i in words:
    race.send_keys(i+' ')
    time.sleep(0.5)