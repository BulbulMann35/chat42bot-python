from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time,os
from time import sleep
import pyautogui
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('chromedriver')
driver.get("https://chat42.online/")
search_bar = driver.find_element_by_id('nickname')
search_bar.clear()
search_bar.send_keys("F19")
#time.sleep(2)
pyautogui.click()
#search_bar.click()
start = driver.find_element_by_id('btn-start')
start.click()
confirm = driver.find_element_by_xpath('/html/body/ons-alert-dialog[2]/div[2]/div/div[3]/ons-alert-dialog-button[2]').click()
def main():
    #time.sleep(1)
    search = driver.find_element_by_xpath('//*[@id="message"]/input')
    #time.sleep(1)
    #for q in range(20):
    #search.send_keys("hey")
    #time.sleep(3)
    #time.sleep(1)
    #pyautogui.press("enter") 
    #search.send_keys("how r u?")
    #pyautogui.press("enter")
    #time.sleep(4)
    #search.send_keys("Where r u from?")
    #time.sleep(8)
    #pyautogui.press("enter")
    #time.sleep(8)
    #search.send_keys("one thing i wanna say you")
    #pyautogui.press("enter")
    #time.sleep(9.5)
    search.send_keys("There are many bots in chat42 you motherfucker")
    #time.sleep(3)
    pyautogui.press("enter")
    driver.find_element_by_id('btn-next').click()
    driver.find_element_by_xpath('/html/body/ons-alert-dialog[2]/div[2]/div/div[3]/ons-alert-dialog-button[2]').click()
    
def main2():
    driver.find_element_by_xpath('/html/body/ons-alert-dialog[2]/div[2]/div/div[3]/ons-alert-dialog-button[2]').click()
    time.sleep(1)
    search = driver.find_element_by_xpath('//*[@id="message"]/input')
    time.sleep(1)
    search.send_keys("hi")
    time.sleep(1)
    pyautogui.press("enter")
    search.send_keys("how r u?")
    time.sleep(5)
    pyautogui.press("enter")
    search.send_keys("Where r u from?")
    time.sleep(7)
    pyautogui.press("enter")
    search.send_keys("watch me naked on pornhub")
    time.sleep(7)
    pyautogui.press("enter")
    time.sleep(8)
    driver.find_element_by_id('btn-next').click()
    driver.find_element_by_xpath('/html/body/ons-alert-dialog[2]/div[2]/div/div[3]/ons-alert-dialog-button[2]').click()
        		
while True:
    time.sleep(1)
    try:
        main()
    except InvalidElementStateException:
        main2()
			
			
			
			
			
			
			
