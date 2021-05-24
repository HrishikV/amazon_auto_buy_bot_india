
from selenium import webdriver as wd
import chromedriver_binary
import requests as tt
from bs4 import  BeautifulSoup
import random
import time
url='url'
wd = wd.Chrome()

wd.implicitly_wait(10)
wd.get(url)
delviy_not_avail='This item cannot be shipped to your selected delivery location. Please choose a different delivery location.'
deleviry=wd.find_element_by_xpath('//*[@id="ddmDeliveryMessage"]').get_attribute('outerHTML')
availa=wd.find_element_by_xpath('//*[@id="availability_feature_div"]').get_attribute('outerHTML')
while True:
    if 'Currently unavailable.' in availa:
        time.sleep(10)
        wd.refresh()
    elif 'In stock.' in availa and delviy_not_avail not in deleviry:
            time.sleep(random.randrange(5.0,10.0))
            buy_now_button=wd.find_element_by_xpath('//*[@id="buy-now-button"]')
            buy_now_button.click()
            time.sleep(random.randrange(5.0,10.0))
            email_input=wd.find_element_by_xpath('//*[@id="ap_email"]')
            email_input.send_keys('user_email')
            email_continue_button=wd.find_element_by_xpath('//*[@id="continue"]')
            email_continue_button.click()
            time.sleep(random.randrange(5,10))
            remember_me_button=wd.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/input')
            remember_me_button.click()
            password_input=wd.find_element_by_xpath('//*[@id="ap_password"]')
            password_input.send_keys('user_password')
            sig_in=wd.find_element_by_xpath('//*[@id="signInSubmit"]')
            sig_in.click()
            time.sleep(random.randrange(5,10))
            pay_on_deleviry_button=wd.find_element_by_xpath('//*[contains(@id, "133")]')

            pay_on_deleviry_button.click()
            time.sleep(random.randrange(5.0,10.0))
            payment_continue_button=wd.find_element_by_xpath('//*[contains(@id, "143")]')
            payment_continue_button.click()
            time.sleep(random.randrange(5.0,10.0))
            palce_your_order_button=wd.find_element_by_xpath('//*[@id="placeYourOrder"]')
            palce_your_order_button.click()
            break
    else:
        wd.refresh()
