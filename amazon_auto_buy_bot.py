
from selenium import webdriver as wd
import chromedriver_binary
import requests as tt
from bs4 import  BeautifulSoup
import random
import time
url='https://www.amazon.in/gp/product/B08FV5GC28/ref=s9_acss_bw_cg_button_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=KAKDEW9KVGWA08DGBEQN&pf_rd_t=101&pf_rd_p=01e9c541-42d0-4ab7-ba81-f69fbb14851b&pf_rd_i=21725163031'
wd = wd.Chrome()

wd.implicitly_wait(10)
wd.get(url)
availa=wd.find_element_by_xpath('//*[@id="availability_feature_div"]').get_attribute('outerHTML')
if 'Currently unavailable.' in availa:
    time.sleep(10)
    wd.refresh()
elif 'In stock.' in availa:
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