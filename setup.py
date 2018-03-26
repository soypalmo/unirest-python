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
        "git+ssh://git@github.com/tirkarthi/python-poster.git@f1bcbc1fe3ffd2d15726d111c9f55fdfc9e33ade#egg=poster-0.8.2"
    ]
)
