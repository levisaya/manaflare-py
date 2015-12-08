from distutils.core import setup
from setuptools import find_packages

setup(
    name='manaflare',
    version='0.1',
    packages=find_packages(),
    url='',
    license='',
    author='Andy Levisay',
    author_email='levisaya@gmail.com',
    description='',
    install_requires=[
        'Django==1.8.6',
        'djangorestframework==3.3.1'
    ]
)
