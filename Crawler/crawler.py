#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Base Web Crawler Object Program
---
"""

# imports packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ==================================

# Begin Crawler object
class Crawler(object):
    def __init__(self, chromeDriverPath:str, startURL:str):
        """
        Base crawler object
        ---

        Args:
        - chromeDriverPath (:obj:`str`) -- -- The path of chrom driver.
        - startURL (:obj:`str`) -- The URL that you want to start.
        """
        print("Opening browser...", end="")
        self.open_browser(chromeDriverPath, startURL)
        print("Done")

    def __del__(self):
        print("Closing browser...", end="")
        self.driver.quit()
        print("Done")

    def open_browser(self, chromeDriverPath:str, url:str):
        """
        Openin browser
        ---

        Args:
        - chromeDriverPath (:obj:`str`) -- The path of chrom driver.
        - url (:obj:`str`) -- The URL that you want to get.
        """
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # chrome_options.add_argument("headless")
        # chrome_options.add_argument("window-size=1920x1080")
        # chrome_options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=chrome_options)

        # Clear all cookies
        self.driver.delete_all_cookies()

        # GET URL
        self.driver.get(url)

# End Crawler object