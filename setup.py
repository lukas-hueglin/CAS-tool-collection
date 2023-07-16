### setup.py ###
from setuptools import setup, find_packages

setup(
    name='cas-tool-collection',
    version='1.0.0',
    description='Collection of CAS tools',
    author='Lukas Hueglin',
    author_email='lukas.hueglin@outlook.com',
    install_requires=[
        'sympy==1.11.1',
        'sympy-plot-backends==1.6.7',
        'matplotlib==3.7.1',
        'plotly==5.13.1',
        'nbformat==5.7.3'
    ]
)
