from setuptools import setup, find_packages

setup(
    name='max30102',
    version='0.1.0',
    packages=find_packages(),
    author='Chen Hong',
    description='MAX30102 heart rate sensor interface',
    install_requires=[
        'smbus2',
        'numpy',
        'RPi.GPIO'
    ],
)