from setuptools import setup

setup(
    name='spectroscopy',
    version='0.1.0',
    packages=['spectroscopy'],
    entry_points={
        'console_scripts': [
            'spectroscopy = spectroscopy.__main__:main'
        ]
    })
