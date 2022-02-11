# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:47:45 2022

@author: StillScripts
"""

from generator.main import generator
from templates.file_types import Files

generator(Files.ATOM, ["Resizer", "Row"])
generator(Files.MOLECULE, ["Grid"])
generator(Files.CONTEXT, ["Board"])


'''generator(Files.ATOM, ["Button", "PageLink", "Tab"])
generator(Files.MOLECULE, ["NavBar", "Tabs"])
generator(Files.TEMPLATE, ["Home", "Contact", "About"])
generator(Files.PAGE, ["Home", "Contact", "About"])
generator(Files.CONTEXT, ["Auth", "Form"])  '''
