from setuptools import setup
import codecs
import os
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.0.1'
DESCRIPTION = 'Ckan-API-Python-Wrapper'
LONG_DESCRIPTION = 'Ckan-API-Python-Wrapper'


# Setting up
setup(
    name='Ckan-API-Python-Wrapper',
    version=VERSION,
    author='Yam Timor',
    description=DESCRIPTION,
    long_description=long_description,
    packages=['Ckan-API-Python-Wrapper'],
    package_dir={'': 'src'},
    install_requires=['requests', 'json', 'pandas'],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)