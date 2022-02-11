# -*- coding: utf-8 -*-

import os

def check_folder(path):
    return os.path.isdir(path)

def make_folder(path):
    os.mkdir(path)
    
def check_or_make(path):
    if not check_folder(path):
        print(f"MAKING FOLDER - {path}")
        make_folder(path)
        
