# coding: UTF-8
# pylint: disable=invalid-name

from selenium import webdriver

browser = webdriver.Firefox()
type(browser)

browser.get('https://google.com/')
browser.quit()