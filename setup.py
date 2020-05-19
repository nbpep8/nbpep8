from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="nbpep8",
    version="0.0.3",
    author="Debanga Raj Neog",
    author_email="debanga88@gmail.com",
    description="A package for PEP8 analysis of notebook cell",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/nbpep8/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
