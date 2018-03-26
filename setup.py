try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Unirest',
    version='1.1.7',
    author='Mashape',
    author_email='opensource@mashape.com',
    packages=['unirest'],
    url='https://github.com/Mashape/unirest-python',
    license='LICENSE',
    description='Simplified, lightweight HTTP client library',
    install_requires=[
        "poster >= 0.8.1"
    ],
    dependency_links=[
        "git+ssh://git@github.com/tirkarthi/python-poster.git@f2ba2ca8013ba5d1c5be2a59926b85f33e82b417#egg=poster-0.8.2"
    ]
)
