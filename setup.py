import os
from setuptools import find_packages,setup

with open(os.path.join(os.path.dirname(__file__),'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
    name='django_miniprogram_api',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app implemented the WeChat miniprogram\'s login, payment and other APIs',
    long_description=README,
    url='https://www.example.com/',
    author='Tinchy',
    author_email='tinchy@yeah.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1', # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        #'Programming Language :: Python',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
   ],
)