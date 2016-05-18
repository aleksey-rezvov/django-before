from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-before',

    version='1.0.0',

    description='Tools that are needed BEFORE any others in each django project',
    long_description=long_description,

    url='https://github.com/alekseyr/django-before',

    author='Aleksey Rezvov',
    author_email='aleksey.rezvov@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
    ],

    keywords='django settings.py',

    packages=['django_before', ],
)
