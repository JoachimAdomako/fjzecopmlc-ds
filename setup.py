"""Setup configuration for fjzecopmlc-ds package."""
from setuptools import setup, find_packages

setup(
    name="fjzecopmlc-ds",
    version="0.1.0",
    description="A simple data structures library",
    author="Joachim Adomako",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
