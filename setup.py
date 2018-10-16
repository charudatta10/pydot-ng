#!/usr/bin/env python
import os
from codecs import open

from setuptools import setup


# NOTE(prmtl): found reason on https://superuser.com/q/259703
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'


with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='pydot_ng',
    version='1.0.1.dev0',
    description='Python interface to Graphviz\'s Dot',
    author='Ero Carrera',
    author_email='ero@dkbza.org',
    maintainer='Sebastian Kalinowski',
    maintainer_email='sebastian@kalinowski.eu',
    url="https://github.com/pydot/pydot-ng",
    license='MIT',
    keywords='graphviz dot graphs visualization',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=readme,
    packages=['pydot_ng'],
    package_dir={'pydot_ng': 'pydot_ng'},
    install_requires=['pyparsing>=2.0.1'],
)
