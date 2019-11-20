#!/usr/bin/env python

import os
import subprocess
from setuptools import setup, find_packages


version = "0.0.1"
sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8") 
package_name = "kaggledatasets"

cwd = os.path.dirname(os.path.abspath(__file__))

def write_version_file():
    version_path = os.path.join(cwd, package_name, "version.py")
    with open(version_path, "w") as f:
        f.write("__version__ = '{}'\n".format(version))
        f.write("git_version = {}\n".format(repr(sha)))

write_version_file()

readme = open("README.md").read()

requirements = open("requirements.txt").read().split()

setup(
    name=package_name,
    version=version,
    author="Omkar Prabhu",
    author_email="prabhuomkar@yandex.com",
    url="https://github.com/kaggledatasets/kaggledatasets",
    description="Collection of Kaggle Datasets ready to use for Everyone",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=find_packages(exclude=("tests",)),
    zip_safe=True,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
