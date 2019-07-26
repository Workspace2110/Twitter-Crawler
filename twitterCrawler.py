#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Twitter Crawler Object Program
---
"""

# imports packages
import time

from bs4 import BeautifulSoup

from selenium.webdriver.common.action_chains import ActionChains

from Crawler.crawler import Crawler
# ==================================

class TwitterCrawler(Crawler):
    def __init__(self, chromeDriverPath:str, userId:str, passwd:str, twitterURL="https://twitter.com/login?lang=en"):
        super(self.__class__, self).__init__(chromeDriverPath, twitterURL)
        self.login(userId, passwd)

    def __del__(self):
        return super(self.__class__, self).__del__()

    def login(self, userId:str, passwd:str):
        usr_field = self.driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
        passwd_field = self.driver.find_element_by_xpath("//input[@class='js-password-field']")
        loginButton = self.driver.find_element_by_xpath("//button[@class='submit EdgeButton EdgeButton--primary EdgeButtom--medium']")

        usr_field.send_keys(userId)
        passwd_field.send_keys(passwd)
        loginButton.submit()
        time.sleep(10)
    
    def search(self, keyword:str):
        pass

    # For post:
    def get_posts(self):
        pass

    def get_post_author(self):
        pass

    def get_post_time(self):
        pass

    def get_post_unixtime(self):
        pass

    def get_post_content(self):
        pass

    def get_post_reply_count(self):
        pass

    def get_post_retweet_count(self):
        pass

    def get_post_likes_count(self):
        pass
    
    def get_post_comments(self):
        pass
    # ==================================

    # For comment:
    def get_post_author(self, postData:BeautifulSoup):
        pass

    def get_comment_time(self):
        pass

    def get_comment_unixtime(self):
        pass

    def get_comment_content(self):
        pass

    def get_comment_reply_count(self):
        pass

    def get_comment_retweet_count(self):
        pass

    def get_comment_likes_count(self):
        pass

    def get_comment_comments(self):
        pass
    # ==================================
