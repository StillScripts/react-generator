# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:47:45 2022

@author: StillScripts
"""

from generator.main import generator
from templates.file_types import Files

atom_files = [
    "BodyText", "Button", "CustomLink", "HeadingText", "Input", "Pill"
    ]
molecule_files = [
    "Header", "Navbar", "Sidebar", "Hero", "SectionHeading", "Feature", 
    "Project", "Testimonial", "TechnologyCard", "BlogCard", "Card", 
    "SocialLinks", "ContactForm", "Footer", "BlogArticle"
    ]
template_files = ["Home", "Technology", "Blog", "BlogPost", "Contact"], 
page_files = ["Technology", "Blog", "Contact"]

# Generate components for portfolio website
generator(Files.ATOM, atom_files)
generator(Files.MOLECULE, molecule_files)
generator(Files.TEMPLATE, template_files)
generator(Files.PAGE, page_files)

