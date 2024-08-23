from setuptools import find_packages, setup
from typing import List

HYPNE_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    
    '''
    get_requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPNE_E_DOT in requirements:
            requirements.remove(HYPNE_E_DOT)
            
    return requirements

setup(
name= 'mlproject',
version = '0.0.1',
author = 'Y0gi',
author_email = 'y1998rathore@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt') 
    
)