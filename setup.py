from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this funtion will return list of experiments
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            '''
            read lines from the line
            
            '''
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirement=line.strip()
                ##ignnore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst



setup(
    name="cyber_security",
    version="0.0.0",
    author="sandeep-sekhar",
    author_email="sekharsandeep4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



