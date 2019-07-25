#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Twitter Crawler Object Program
---
"""

# imports packages
from Crawler.crawler import Crawler
# ==================================

class TwitterCrawler(Crawler):
    def __init__(self, chromeDriverPath:str, twitterURL="https://twitter.com"):
        super(self.__class__, self).__init__(chromeDriverPath, twitterURL)

    def __del__(self):
        return super(self.__class__, self).__del__()

    def login(self):
        pass
    
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
    def get_post_author(self):
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
