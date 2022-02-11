# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:28:26 2022

@author: danie
"""

def create_file(path, content):
    index_file = open(path, 'w')
    index_file.write(content)
    index_file.close
    print(f"MAKING FILE - {path}")