# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='computils',
    version='0.0.1',
    description='Unix utilities that emphasize composition',
    long_description=readme,
    author='Paulus Esterhazy',
    author_email='pesterhazy@gmail.com',
    url='https://github.com/pesterhazy/computils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

