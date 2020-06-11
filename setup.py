import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyportmgmt",
	version="0.0.1",
	author="Srinivasa Balaji",
	author_email="rsbbalaji19@gmail.com",
	description="A package for researchers in the domain Portfolio Management",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/RSB-Balaji/PyPortfolioMgmt",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)