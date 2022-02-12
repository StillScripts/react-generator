# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:19:14 2022

@author: danie
"""

def get_template(file_name):
    template = f'export interface {file_name}Props'
    template += ' {}\n\n'
    template += f'const {file_name}: React.FC<{file_name}Props> = ('
    template += '{ children }) => (\n  <div className="">{children}</div>\n);\n\n'
    template += f'export default {file_name};\n'
    return template
    
    