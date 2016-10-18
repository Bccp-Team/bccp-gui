#!/usr/bin/python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='bccp_gui',

    version='1.0',

    description='tiny webapp for bccp',

    license = "Beerware",

    packages=['bccp_gui'],

    install_requires=[
        'docopt',
        'requests',
        'flask',
        'grpcio'
    ],

    entry_points={
        'console_scripts': [
            'bccp_gui=bccp_gui.__init__:main'
            ]
        }
)
