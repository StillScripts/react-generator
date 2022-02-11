# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:55:40 2022

@author: danie
"""

from enum import Enum

class Files(Enum):
    ATOM = 1 # Single HTML element - e.g. Button
    MOLECULE = 2 # Combination of elements - e.g. Card
    TEMPLATE = 3 # Layout/Sections of a page
    PAGE = 4 # Next.js page file
    CONTEXT = 5 # React.Context file
    PROVIDER = 6 # React.Context provider file   