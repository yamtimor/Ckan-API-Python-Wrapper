from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Ckan-API-Python-Wrapper'
LONG_DESCRIPTION = 'Ckan-API-Python-Wrapper'

# Setting up
setup(
    name="Ckan-API-Python-Wrapper",
    version=VERSION,
    author="Yam Timor",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = ['requests', 'json', 'pandas']
)