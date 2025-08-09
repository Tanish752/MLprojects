from setuptools import setup, find_packages

def get_requirements():
	with open('requirements.txt') as f:
		requirements = f.read().splitlines()
		requirements = [req for req in requirements if req.strip() != '-e .']
		return requirements
		

setup (
	name='MLproject',
	version='0.1.1',
	author='Tanish',
	author_email='tanish752@gmail.com',
	packages=find_packages(),
	install_requires=get_requirements()
)