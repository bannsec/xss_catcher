# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = "See website for more info."

setup(
    name='xss_catcher',
    version='0.0.2',
    description='Simple pythonic script to catch Cross Site Scripting (XSS) connections',
    long_description=long_description,
    url='https://github.com/owlz/xss_catcher',
    author='Michael Bann',
    author_email='self@bannsecurity.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],
    keywords='xss',
    packages=find_packages(exclude=['contrib', 'docs', 'tests','dist']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'xss_catcher = xss_catcher.xss_catcher:main',
        ],
    },

)

