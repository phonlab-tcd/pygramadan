# coding=UTF-8
from setuptools import find_packages, setup

setup(
    name='pygramadan',
    packages=find_packages(exclude=("scripts",)),
    version='0.0.1',
    description='Library for working with Bunachar Náisiúnta Moirfeolaíochta',
    author='',
    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
          'lxml',
          'pytest',
      ],
)
