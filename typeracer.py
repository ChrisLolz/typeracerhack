from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Welcome to the type racer hack made by Chris, start a race and watch the magic happen.\nReminder: Don't go in and out of races or else you might break the program")

hello = input("Paste the file location of the chromedriver.exe below: (I recommend you put it in the documents folder)\n")
path = (f"{hello}")
driver = webdriver.Chrome(path)
driver.get("https://play.typeracer.com")
driver.maximize_window()

while True:
    target = input("What is your target Words Per Minute? ")
    try:
        target = int(target)
        break
    except ValueError:
        print("Please type an integer")

while True:
    try:
        stuff = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//span[@unselectable= 'on']")))
        words = []
        for i in stuff:
            words.append(i.text)
        if len(words) == 3:
            words[0] = words[0] + words[1]
            words.pop(1)

        words = ' '.join(words)
        words = words.split()
        if words[1] == ",":
            words[0] = words[0] + words[1]
            words.pop(1)
        speed = (((len(words)*60)/target)/len(words))-0.01

        if not words:
            continue

        race = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))

        while True:
            try:
                for i in words:
                    race.send_keys(i + ' ')
                    time.sleep(speed)
                break
            except:
                time.sleep(0.1)

        bye = input("Do you want to quit? Y for Yes and N for No")
        if bye == "Y" or bye == "y":
            driver.quit()
            break
        while True:
            target = input("What is your target Words Per Minute? ")
            try:
                target = int(target)
                break
            except ValueError:
                print("Please type an integer")
    except:
        time.sleep(1)
