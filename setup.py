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
        'Django>=1.8',
        'path.py',
        'django-model-utils>=2.6',
        'gunicorn',
        'django-bootstrap3>=7',
        'dj-database-url',
        'dj-static',
        'psycopg2',
        'django-extensions',
        'requests==2.12.4',
        'requests-mock==1.2.0',
        'redis==2.10.5',
        'celery==4.0.2',
        'kombu==4.0.2',
        'django-celery-beat==1.0.1',
        'django-celery-results==1.0.1',
        'django-redis==4.6.0',
        'django-choices==1.4.4',
        'django-adminlte2',
        'django-hordak>=1.2.0',
    ],
    # Ensure we include files from the manifest
    include_package_data=True,
)
