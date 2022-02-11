import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'react-generator/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "react-generator",        # what you want to call the archive/egg
    version = version,
    packages=["react-generator"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'react-generator[foo]'
    package_data = {"react-generator": ["VERSION.txt"]},
    author="Daniel Still",
    author_email = "daniel@stillscripts.com",
    description = "Generate React components rapidly",
    license = "Apache 2.0",
    keywords= "example documentation tutorial",
    url = "http://github.com/StillScripts"
)
