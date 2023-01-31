import subprocess

import setuptools

version = subprocess.check_output([
    "git",
    "describe",
    "--abbrev=0",
]).strip().decode()

commit = subprocess.check_output([
    "git",
    "rev-parse",
    "HEAD",
]).strip().decode()

with open('rave/__version__.py', 'w') as init:
    init.write(f"version = \"{version}\"\n")
    init.write(f"commit = \"{commit}\"\n")

with open("README.md", "r") as readme:
    readme = readme.read()

with open("requirements.txt", "r") as requirements:
    requirements = requirements.read()

setuptools.setup(
    name="acids-rave",
    version=version,
    author="Antoine CAILLON",
    author_email="caillon@ircam.fr",
    description="RAVE: a Realtime Audio Variatione autoEncoder",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={
        'rave/configs': ['*.gin'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": [
        "rave = scripts.main_cli:main",
    ]},
    install_requires=requirements.split("\n"),
    python_requires='<=3.8',
    include_package_data=True,
)
