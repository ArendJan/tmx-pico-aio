#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()


setup(
    name='tmx-pico-aio',
    packages=['tmx_pico_aio'],
    install_requires=['pyserial', 'aioserial'],

    version='1.3',
    description="Remotely Control And Monitor A Raspberry Pi Pico Using Asyncio",
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    url='https://github.com/MrYsLab/tmx-pico-aio',
    download_url='https://github.com/MrYsLab/tmx-pico-aio',
    keywords=['telemetrix', 'Raspberry_Pi_Pico', 'Protocol', 'Python', 'asyncio'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

