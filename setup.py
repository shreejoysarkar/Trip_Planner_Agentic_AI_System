from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''Reads the requirements from a file and returns them as a list.'''

    requirement_list: List[str] = []

    try:
        ## Open and read the requirements.txt 
        with open("requirements.txt", 'r') as file:
            ## Read lines from file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                ## Strip whitespace and ignore empty lines
                requirement = line.strip()
                ## ignore -e 
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

    return requirement_list

print(get_requirements)
setup(
    name='Trip_planner',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)