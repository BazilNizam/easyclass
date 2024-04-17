from setuptools import setup

setup(
    name='pyextend',
    version='0.1.0',
    packages=['pyextend'],
    entry_points={
        'console_scripts': [
            'pyextend=pyextend.interpreter:main',
        ],
    }
)
