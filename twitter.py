#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Twitter Crawler Program
---
"""

# imports packages

from twitterCrawler import TwitterCrawler
# ==================================

def main():
    # Configures:
    chromeDriverPath = "./chromedriver.exe"
    email = "workspace2110@gmail.com"
    passwd = "c39CH56D36"
    # ==================================

    TwitterCrawler(chromeDriverPath, email, passwd)

if __name__ == '__main__':
    main()
    