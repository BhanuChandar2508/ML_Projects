## Setting up the setup.py file so that our packages gets installed through this application
## and later on we can use this to commit/deploy into the python pypi, so that everyone can import it

from setuptools import find_packages,setup
from typing import List




HYPHEN_E_DOT='-e .'
## Function to fetch the requirement.txt file which contains the installation libraries list:
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of
    '''
    requirements=[]
    with open('requirements.txt') as file_list:
        requirements=file_list.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='BHANU CHANDAR',
    author_email='polojubhanuchandar667@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)