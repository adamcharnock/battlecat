#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='battlecat',
    version=open('VERSION').read().strip(),
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/adamcharnock/battlecat',
    license='MIT',
    description='Django-based double entry accounting based on Hordak',
    long_description=open('README.rst').read() if exists('README.rst') else '',
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        'django>=1.8',
        'django-hordak>=1.2.0',
        'path.py',
        'django-model-utils>=2.5.0',
        'gunicorn',
        'django-bootstrap3>=7',
        'dj-database-url',
        'dj-static',
        'psycopg2',
        'django-extensions',
        'celery>=3.1,<4',
        'django-celery>=3.1',
        'django-import-export>=0.5.0',
        'six',
        'python-dateutil',
        'django-adminlte2>=0.1.5',
    ],
    # Ensure we include files from the manifest
    include_package_data=True,
)
