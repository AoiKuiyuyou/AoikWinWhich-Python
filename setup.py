# coding: utf-8
import os
from setuptools import find_packages
from setuptools import setup

#
setup(
    name='AoikWinWhich',

    version='0.1',

    description="""Windows version of Linux's "which" program.""",

    url='https://github.com/AoiKuiyuyou/AoikWinWhich',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='windows which',

    package_dir = {'':'src'},

    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoikwinwhich=aoikwinwhich.aoikwinwhich:main',
        ],
    },
)
