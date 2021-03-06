#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='TTools',
    version='0.1.0',
    author="Tomasz W. Turowski",
    author_email="twturowski@gmail.com",
    description='TBA',
    long_description=open('README.md').read(),
    license='LICENSE.txt',
    # keywords="board games AI artificial intelligence negamax",
    packages=setuptools.find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent"],
    scripts=['scripts/SAM2profiles.py',
             'scripts/mergeSalmon.py',
             'scripts/csv2pickle.py'],
    python_requires='>=3.6'
)