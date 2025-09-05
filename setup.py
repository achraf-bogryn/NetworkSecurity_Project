# this file responsable to build my ML application as package .building our application as package
from setuptools import setup, find_packages
from typing import List 


HYPEN_E_DOT = '-e .'
def get_requiremnts()->List[str]:
    """
    this function will return the list of requirements
    """
    requirements_lst : List[str] = []
    try :
        with open('requirements.txt','r') as file_obj:
          #   Read Lines from the file
            lines = file_obj.readlines()
          #   Process each line to remove whitespace and newline characters
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != HYPEN_E_DOT:
                  requirements_lst.append(requirements)
     
    

    except FileNotFoundError:
        print("requirements.txt file not found")
  
    return requirements_lst




setup (
name= "networksecurity",
version= "0.0.1",
author= "Achraf Bogryn",
author_email= "achrafbogryn12345@gmail.com",
packages= find_packages(),
install_requires =  get_requiremnts()    
     
     
     )