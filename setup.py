from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="healthchecks",
    version="0.0.1",
    description="simple functions for interacting with healthchecks.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Davis Busteed",
    author_email="davis.busteed@rxa.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
)
