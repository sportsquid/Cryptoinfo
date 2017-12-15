from setuptools import setup
setup(
    name='cryptoinfo',
    version='0.5',
    author='sportsquid',
    
    description='Get prices of cryptocurrencies from the command line',
    url='https://github.com/sportsquid/Cryptoinfo',
    long_description='A simple python program allowing users to find the prices of popular cryptocurrencies from the command line.',
    py_modules=['cryptoinfo'],
    entry_points={
        'console_scripts': [
            'cryptoinfo = cryptoinfo:main'
        ]
    },
)
