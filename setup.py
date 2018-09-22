#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = ['Click>=6.0', 'path.py>=11.0']

SETUP_REQUIREMENTS = ['pytest-runner', ]

TEST_REQUIREMENTS = ['pytest', ]

setup(
    author="Aubrey Taylor",
    author_email='aubricus@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="'Clack' [klak]: A sharp sound or series of sounds.",
    entry_points={
        'console_scripts': [
            'klak=klak.cli:main',
        ],
    },
    install_requires=REQUIREMENTS,
    license="MIT License",
    long_description=README + '\n\n' + HISTORY,
    include_package_data=True,
    keywords='klak',
    name='klak',
    packages=find_packages(include=['klak']),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url='https://github.com/aubricus/klak',
    version='0.2.4',
    zip_safe=False,
)
