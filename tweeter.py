from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import giphs as GIF

driver = webdriver.Chrome(
    executable_path="/Users/12533/Downloads/chromedriver_win32/chromedriver")
driver.get("https://twitter.com/")
sleep(3)
driver.find_element_by_name(
    "session[username_or_email]").send_keys("mariners2023")
driver.find_element_by_name("session[password]").send_keys("Gemini253!")
driver.find_element_by_name("session[password]").send_keys(Keys.RETURN)
sleep(3)

driver.find_element_by_xpath(
    "//a[@data-testid='SideNav_NewTweet_Button']").click()
sleep(1)
driver.find_element_by_class_name("notranslate").click()
driver.find_element_by_class_name("notranslate").send_keys(GIF.get_gif())
