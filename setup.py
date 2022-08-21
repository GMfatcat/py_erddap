#!/usr/bin/env python
# coding: utf-8

from setuptools import setup,find_packages

setup(
    name='py_erddap',
    version='1.0.1',
    author='GMfatcat',
    author_email='a60102244@gmail.com',
    url='https://github.com/GMfatcat/py_erddap',
    description='Package contains handy and customize tool for downloading grid data from ERDDAP website with API',
    packages = find_packages(),
    install_requires=['requests', 'xarray', 'aiohttp'],
    license='MIT License',
    platforms=["all"]

    )