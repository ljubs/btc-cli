from setuptools import setup

setup(
    name='btc',
    py_modules=['btc'],
    entry_points={
        'console_scripts': [
            'btc=btc:main',
        ],
    },
    install_requires=['requests'],
)