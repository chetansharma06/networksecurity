'''
the setup.py file is an essential part of packaging and distributing Python projects
. It contains information about the package, such as its name, version, author, and any dependencies it requires. This file is used by tools like setuptools and pip to build and install the package.

'''
from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty line and -e
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("The requirements.txt file is not found.")
    return requirement_lst
print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Chetan Sharma",
    author_email="chetansharma5387@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
