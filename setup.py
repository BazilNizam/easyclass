from setuptools import setup, find_packages
import os

# Optional: Load long description from README.md
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ezcls',
    version='0.2.2',
    description='A python package helps in repeating your print statements and calling classes as much as you needed with *',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BazilNizam/easyclass',
    author='Bazil Nizam',
    author_email='bazil_nizam@yhoo.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'easypy=easypy.interpreter:main',
        ],
    },
)
