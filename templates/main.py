# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:33:05 2022

@author: danie
"""


from templates import atom
from templates import molecule
from templates import template
from templates import page
from templates import context
from templates import provider
from templates import file_types
Files = file_types.Files


def get_template(file_type, file_name):
    if file_type == Files.ATOM:
        return atom.get_template(file_name)
    elif file_type == Files.MOLECULE:
        return molecule.get_template(file_name)
    elif file_type == Files.TEMPLATE:
        return template.get_template(file_name)
    elif file_type == Files.PAGE:
        return page.get_template(file_name)
    elif file_type == Files.CONTEXT:
        return context.get_template(file_name)
    elif file_type == Files.PROVIDER:
        return provider.get_template(file_name)
    
print(get_template(Files.ATOM, "Button"))
