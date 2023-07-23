from setuptools import setup, find_packages
from typing import List 


#Declaring variables for set up functions 
Project_Name= "housing-predictor"
Version='0.0.2'
Author = "neoman"
Description = 'This is my first machine learning Project '
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirments_list()->List[str]:

    """
    Description : this function will return requirements mentioned in requirements.txt file 
    returns a list which contains names of libraries mentioned in requirements.txt file 
    """
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    



setup(
name = Project_Name,
version= Version,
author= Author,
description=Description,
packages = find_packages(), 
install_requires = get_requirments_list()

)

