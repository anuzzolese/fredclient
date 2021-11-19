from setuptools import setup, find_packages

install_requires=[
   'rdflib'
]

setup(name='fredclient', version='1.0.0',
    packages=find_packages(), install_requires=install_requires)
