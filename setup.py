from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    get list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readline()
        requirements = [req.replace('\n',"") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name = "sentiments_analysis",
    version= "0.0.1",
    author= "Dipesh",
    author_email="dpsh.dhote@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')



)