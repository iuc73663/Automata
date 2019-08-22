# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:11:15 2019

@author: Administrator
"""

import praw

reddit = praw.Reddit(client_id='my client id',
                     client_secret='my client secret',
                     user_agent='my user agent')