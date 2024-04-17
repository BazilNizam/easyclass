from setuptools import setup, find_packages

setup(
    name='easypy',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'easypy=easypy.interpreter:main',
        ],
    },
    license='MIT',
    author='Bazil Nizam',
    author_email='bazil_nizam@yhoo.com',
    description='A python package helps in repeating your print statements and calling classes as much as u needede with * ',
    keywords='easypy',
    url='https://github.com/BazilNizam/easyclass',  # Optional
)
