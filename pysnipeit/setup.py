from setuptools import setup,find_packages
import os

with open('README.md') as fh:
    LONG_DESCRIPTION = fh.read()
    
setup(
    name='pysnipeit',
    version='0.0.1',
    description='Python library to interface with SNIPE_IT\'s API',
    author='Jeff Latta',
    url='',
    classifiers=[],
    packages=find_packages(),
    install_requires=['requests'],

)