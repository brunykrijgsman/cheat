# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Cheat',
    url='https://github.com/brunykrijgsman/cheat',
    author='Bruny Krijgsman',
    author_email='bruny.krijgsman@student.uva.nl',
    # Needed to actually package something
    packages=['src'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)