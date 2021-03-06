# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='njit-alg-scratch',
    version='0.1.0',
    description='NJIT algorithms course',
    python_requires='==3.*,>=3.7.0',
    author='Shawn Cicoria',
    author_email='github@cicoria.com',
    license='MIT',
    packages=[],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'autopep8==1.*,>=1.5.3', 'flake8==3.*,>=3.8.2',
        'jupyterlab==2.*,>=2.1.3', 'matplotlib==3.*,>=3.2.1',
        'numpy==1.*,>=1.18.4', 'pandas==1.*,>=1.0.3',
        'scikit-learn==0.*,>=0.23.1'
    ],
)
