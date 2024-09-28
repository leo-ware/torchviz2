#!/usr/bin/env python
import os
import shutil
import sys
from setuptools import setup, find_packages

VERSION = '0.0.2'

with open('README.md', 'r') as f:
    long_description = f.read()

setup_info = dict(
    # Metadata
    name='torchviz2',
    version=VERSION,
    author='Leo Ware',
    author_email='leoware@gmail.com',
    
    # url='https://github.com/pytorch/pytorchviz',
    description='A small package to create visualizations of PyTorch execution graphs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',

    # Package info
    packages=find_packages(exclude=('test',)),

    zip_safe=True,

    install_requires=[
        'torch',
        'graphviz',
        'looseversion'
    ]
)

setup(**setup_info)
