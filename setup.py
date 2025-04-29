from setuptools import find_packages,setup
from typing import List

# def get_requirements(file_path):
#     with open(file_path) as file:
#         return file.read().splitlines()

HYPHEN_E_DOT='-e .'
    
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='mlproject',
    version='0.0.1',
    author='yogesh',
    author_email='yogiafse@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)