#!/usr/bin/env python

from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name = 'stistarg',
    url = 'http://www.stsci.edu/instruments/stis/',
    version = '2.1',
    description = 'HST/STIS Target Acquisition Simulator',
    long_description = long_description,
    author = 'Sean Lockwood, Bralen Berry',
    author_email = 'help@stsci.edu',
    maintainer = 'Sean Lockwood',
    maintainer_email = 'lockwood@stsci.edu',
    license = 'BSD-new',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Development Status :: 4 - Beta',
                   'Operating System :: OS Independent',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Scientific/Engineering :: Astronomy',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
    packages = ['stistarg'],
    install_requires = ['setuptools', 'numpy', 'astropy', 'matplotlib'],
    entry_points={
          'console_scripts': ['stistarg = stistarg.stistarg:parse']},
    )
