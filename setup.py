from setuptools import find_packages, setup
from typing import List 

FLAG = '-e .'
def get_requirements(path: str) -> List[str]:
	requirements = []
	with open(path) as file:
		requirements = file.readlines()
		# Remove newline characters from requirements list
		requirements = [req.replace("\n", "") for req in requirements]
		# Remove the -e . flag, which is not a library but a trigger
		if FLAG in requirements:
			requirements.remove(FLAG)
	return requirements

setup(
	name='Telco Customer Churn Prediction',
	version='0.0.1',
	author='Niranjanky',
	author_email='niranjanky14@gmail.com',
	packages=find_packages(),
	install_requires=get_requirements('requirements.txt'),
)




	

