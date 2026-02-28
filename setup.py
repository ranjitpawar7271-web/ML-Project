from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read requirements file and return list of dependencies."""
    with open(file_path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    return [req for req in requirements if req != "-e ."]

setup(
    name="mlproject",
    version="0.0.1",
    author="Ranjit Pawar",
    author_email="ranjitpawar7271@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)