# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="textxgen",
    version="1.0.4",
    author="Sohail Shaikh",
    author_email="support@pystack.site",
    description="A Python package for interacting with models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pystack.site/",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
