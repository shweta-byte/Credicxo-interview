# Bonus Task
# 1. Write script that fills the small reporting form. 
# 2. It must bypass the google's reCaptchaV2 and then submit the form successfully.

import os
import random
import time

# selenium libraries
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys



web  = webdriver.Chrome()
web.get('https://safebrowsing.google.com/safebrowsing/report_phish/')

url_filled = "https://www.flipkart.com/"
url = web.find_element_by_xpath('//*[@id="url"]')
url.send_keys(url_filled)

additional = 'looks like it is not the real official site'
optional_textbox = web.find_element_by_xpath('//*[@id="dq"]')
optional_textbox.send_keys(additional)

#click i am not a robo check box
#checkbox = web.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
#checkbox.click()

#switch to recaptcha audio control frame
#web.switch_to.default_content()
#frames= web.find_element_by_xpath('')

submit_report = web.find_element_by_xpath('//*[@id="formprincipal"]/div[4]/input')
submit_report.click()
