from setuptools import setup, find_packages
from typing import List

hyphen = '-e .'

def get_requirements(file_path: str) -> list:
    
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if hyphen in requirements:
            requirements.remove(hyphen)

    return requirements

setup(
    name='codebase_ml',
    version='0.0.1',
    description='ml code dump structure',
    author='RA',
    author_email='ra@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt') 
)