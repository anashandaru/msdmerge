from setuptools import setup

setup(
    name='merge',
    version='0.1.0',
    py_modules=['merge'],
    install_requires=[
        'Click',
        'obspy',
    ],
    entry_points={
        'console_scripts': [
            'merge = merge:main',
        ],
    },
)