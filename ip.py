from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import socket
args =  sys.argv
arg = args[1:]
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
try:
    socket.gethostbyname('freenom.com')
except socket.error:
    print('not resolved')
    exit()
print('resolved')
browser.get('https://my.freenom.com/clientarea.php?managedns=serverroom.tk&domainid=1127870232')
element = browser.find_element_by_id('username')
element.send_keys('kacperszkola365@gmail.com')
element = browser.find_element_by_id('password')
element.send_keys('ayLAvAT2gx7TGDA')
sleep(5)
try:
    element = browser.find_element_by_xpath('//input[@type="submit" and @value="Login"]')
    element.click()
    sleep (5)
    element = browser.find_element_by_xpath('//input[@type="text" and @name="records[0][value]"]')
    element.clear()
    element.send_keys(arg)
    sleep (5)
    element = browser.find_element_by_xpath('//button[@style="margin: 0px 10px 20px 5px; font-weight: 600; float:right;"]')
    element.click()
    sleep(5)
    browser.quit()
except:
    print("dns managmnet unavalible")
    browser.quit()
