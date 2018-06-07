#-*-coding:utf-8 -*-
from selenium import webdriver
import time
import unittest
class Ecercise(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.url="http://test1.zmninfo.com/SimulationElement/"
        self.browser.implicitly_wait(int(20))
        #self.browser.maximize_window()
    def tearDown(self):
        #self.browser.quit()
        pass

    def test_lianxi(self):
        browser=self.browser
        browser.get(self.url)
        '''
        browser.find_element_by_name("t1").send_keys("lalala")
        time.sleep(3)

        #进行勾选
        checkboxs=browser.find_elements_by_xpath("//input[@type='checkbox']")
        for checkbox in checkboxs:
            checkbox.click()
        time.sleep(2)
        '''

