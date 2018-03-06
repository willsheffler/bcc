#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'traitlets',
]

setup_requirements = ['pytest-runner', ]

test_requirements = [
    'pytest',
    'numpy',
    'traitlets',
]

setup(
    author="Will Sheffler",
    author_email='willsheffler@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="N-dim invertible BCC lattice",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bcc',
    name='bcc',
    packages=find_packages(include=['bcc']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/willsheffler/bcc',
    version='0.1.5',
    zip_safe=False,
)
